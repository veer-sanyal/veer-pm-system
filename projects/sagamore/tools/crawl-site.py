#!/usr/bin/env python3
"""Crawl sagamorebsa.org and produce the evidence table the website audit links against.

Why this exists: the audit's value to Bryon is "here is the page, here is the line, here is
the fix." That needs real URLs and real counts, not recollection. Every number in the
website audit should be reproducible by running this.

The site is server-rendered WordPress, so plain HTTP is enough — no browser needed. The two
things that DO need a browser (what renders at 375px, and screenshots) are handled by
tools/capture-audit-screenshots.sh.

Run:  python3 projects/sagamore/tools/crawl-site.py
Out:  projects/sagamore/build/site-inventory.json  + a summary on stdout
"""

import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = "https://sagamorebsa.org"
APP = "https://sagamorebsa.org/htdocs/wordpress"
OUT = Path(__file__).resolve().parent.parent / "build" / "site-inventory.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/151 Safari/537.36"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

STALE_YEARS = ("2022", "2023", "2024", "2025")


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.getcode(), r.read().decode("utf-8", "ignore"), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", url
    except Exception as e:
        return 0, f"ERROR {type(e).__name__}: {e}", url


def visible_text(html):
    t = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&nbsp;?", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def analyse(url, html):
    text = visible_text(html)
    imgs = re.findall(r"<img[^>]*>", html, re.I)
    no_alt = [i for i in imgs if not re.search(r'\balt\s*=\s*"[^"]+"', i)]
    hrefs = re.findall(r'href="([^"]+)"', html, re.I)
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    meta = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', html, re.I)
    return {
        "url": url,
        "title": (title.group(1).strip() if title else None),
        "meta_description": (meta.group(1) if meta else None),
        "text_chars": len(text),
        "images_total": len(imgs),
        "images_without_alt": len(no_alt),
        "links_total": len(hrefs),
        "links_to_join": sum(1 for h in hrefs if "/join" in h.lower()),
        "dollar_figures": sorted(set(re.findall(r"\$\s?\d[\d,]*(?:\.\d\d)?", text)))[:12],
        "mentions_join_word": len(re.findall(r"\bjoin\b", text, re.I)),
        "stale_years": sorted({y for y in STALE_YEARS if re.search(rf"\b{y}\b", text)}),
        "beascout_org_links": sum(1 for h in hrefs if "beascout.org" in h.lower()),
        "chrome_extension_links": sum(1 for h in hrefs if "chrome-extension" in h.lower()),
        "http_not_https_links": sum(1 for h in hrefs if h.startswith("http://")),
    }


def discover():
    """Follow the site's own navigation one level deep. Good enough: the nav is the site."""
    seen, queue, pages = set(), [f"{APP}/"], []
    code, html, _ = fetch(f"{APP}/")
    if code == 200:
        for h in re.findall(r'href="([^"]+)"', html, re.I):
            full = urllib.parse.urljoin(f"{APP}/", h).split("#")[0].rstrip("/")
            if full.startswith(APP) and not re.search(r"\.(pdf|jpe?g|png|zip|docx?|xlsx?)$", full, re.I):
                if full not in seen:
                    seen.add(full)
                    queue.append(full + "/")
    for url in queue[:45]:
        code, html, final = fetch(url)
        if code == 200 and html:
            pages.append(analyse(final, html))
            print(f"  {code}  {final}", file=sys.stderr)
        else:
            pages.append({"url": url, "http_status": code, "error": True})
            print(f"  {code}  {url}  <-- non-200", file=sys.stderr)
    return pages


def probe_claims():
    """Directly re-verify the specific claims the audit makes."""
    checks = {}
    for label, url in [
        ("bare_domain_join_404", f"{ROOT}/join/"),
        ("real_join_page", f"{APP}/join/"),
        ("beascout_org_redirect", "http://www.beascout.org/"),
        ("beascout_scouting_org", "https://beascout.scouting.org/"),
        ("campbuffalo_new_subdomain", "http://www.new.campbuffalo.com/"),
        ("campbuffalo_working", "http://campbuffalo.com/"),
    ]:
        code, _, final = fetch(url, timeout=15)
        checks[label] = {"requested": url, "status": code, "resolved_to": final}
    return checks


if __name__ == "__main__":
    print("Crawling…", file=sys.stderr)
    pages = discover()
    claims = probe_claims()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"pages": pages, "claim_checks": claims}, indent=2))

    ok = [p for p in pages if not p.get("error")]
    print(f"\n{len(ok)} pages crawled -> {OUT}")
    print(f"  pages with NO meta description : {sum(1 for p in ok if not p['meta_description'])}/{len(ok)}")
    print(f"  images total / without alt      : {sum(p['images_total'] for p in ok)} / {sum(p['images_without_alt'] for p in ok)}")
    print(f"  pages linking to /join/         : {sum(1 for p in ok if p['links_to_join'])}")
    print(f"  pages with a stale year in text : {sum(1 for p in ok if p['stale_years'])}")
    print(f"  pages with http:// links        : {sum(1 for p in ok if p['http_not_https_links'])}")
    print("\nclaim checks:")
    for k, v in claims.items():
        print(f"  {k:28} {v['status']}  {v['resolved_to']}")
