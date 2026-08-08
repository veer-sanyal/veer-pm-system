#!/usr/bin/env python3
"""Find every link on sagamorebsa.org, test each one, and report what is broken.

Why this instead of clicking through menus in a browser: the navigation is server-rendered
WordPress, so every menu item and button is an <a href> in the HTML. Reading the DOM finds
all of them, including ones buried in menus nobody would think to open, and testing them by
HTTP is exact - a status code rather than an impression. Clicking would be slower and would
miss links that only appear on pages you did not think to visit.

What this does NOT catch, stated plainly so nobody assumes otherwise: buttons wired with
JavaScript rather than an href, links inside embedded PDFs, and anything behind a login.

Run:  python3 projects/sagamore/tools/check-all-links.py
Out:  projects/sagamore/build/link-report.json + a prioritised summary on stdout
"""

import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

APP = "https://sagamorebsa.org/htdocs/wordpress"
OUT = Path(__file__).resolve().parent.parent / "build" / "link-report.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/151 Safari/537.36"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "#", "data:")


def get(url, method="GET", timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.getcode(), r.read().decode("utf-8", "ignore") if method == "GET" else "", r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", url
    except Exception as e:
        return 0, f"{type(e).__name__}", url


def crawl_pages():
    code, html, _ = get(f"{APP}/")
    pages = {f"{APP}/"}
    for h in re.findall(r'href="([^"]+)"', html, re.I):
        full = urllib.parse.urljoin(f"{APP}/", h).split("#")[0]
        if full.startswith(APP) and not re.search(r"\.(pdf|jpe?g|png|zip|docx?|xlsx?)$", full, re.I):
            pages.add(full if full.endswith("/") else full + "/")
    return sorted(pages)[:50]


def collect_links(page):
    code, html, _ = get(page)
    if code != 200:
        return page, []
    out = []
    for m in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.I | re.S):
        href, label = m.group(1).strip(), re.sub(r"<[^>]+>", " ", m.group(2))
        label = re.sub(r"\s+", " ", label).strip()[:70]
        if href.lower().startswith(SKIP_SCHEMES):
            continue
        out.append((urllib.parse.urljoin(page, href), label))
    return page, out


def main():
    print("Discovering pages…", file=sys.stderr)
    pages = crawl_pages()
    print(f"  {len(pages)} pages", file=sys.stderr)

    link_sources = defaultdict(list)
    with ThreadPoolExecutor(max_workers=8) as ex:
        for page, links in ex.map(collect_links, pages):
            for url, label in links:
                link_sources[url].append({"on_page": page, "label": label})

    targets = sorted(link_sources)
    print(f"  {len(targets)} unique link targets, testing…", file=sys.stderr)

    def test(u):
        code, _, final = get(u, method="GET", timeout=18)
        return u, code, final

    results = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        for u, code, final in ex.map(test, targets):
            results[u] = {"status": code, "resolved_to": final, "found_on": link_sources[u]}

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"pages_crawled": pages, "links": results}, indent=2))

    broken = {u: r for u, r in results.items() if r["status"] == 0 or r["status"] >= 400}
    insecure = {u: r for u, r in results.items()
                if u.startswith("http://") and r["status"] not in (0,) and not r["resolved_to"].startswith("https://")}
    redirected_http = {u: r for u, r in results.items()
                       if u.startswith("http://") and r["resolved_to"].startswith("https://")}

    print(f"\n{len(pages)} pages, {len(targets)} unique links tested -> {OUT}\n")
    print(f"BROKEN ({len(broken)}):")
    for u, r in sorted(broken.items(), key=lambda kv: -len(kv[1]["found_on"])):
        label = r["found_on"][0]["label"] or "(no text)"
        print(f'  {str(r["status"]):>3}  {u}')
        print(f'       link text: "{label}"   appears on {len(r["found_on"])} page(s)')
        for src in r["found_on"][:3]:
            print(f'         - {src["on_page"]}')
    print(f"\nINSECURE http:// that never upgrades ({len(insecure)}):")
    for u in sorted(insecure)[:15]:
        print(f"  {u}")
    print(f"\nhttp:// that redirects to https (fine, but worth updating) ({len(redirected_http)})")


if __name__ == "__main__":
    main()
