#!/usr/bin/env python3
"""Re-verify the council's own broken links, carefully, one at a time.

The first pass reported 196 broken links out of 469. Most of that was the checker's own
fault and would have been humiliating in front of a client:

  * status 0 on pages that load perfectly when requested on their own (concurrency timeouts)
  * 429 from scouting.org, which was rate-limiting the crawler, not serving a dead page
  * 400 from facebook.com, which blocks non-browser requests
  * 400 from scoutingevent.com because HTML entities in the href were never decoded

So this script does the opposite of the first one: council-owned URLs only, sequential,
entity-decoded, two retries with a pause, and a browser User-Agent. Slow on purpose. A
number in a client document has to survive being checked.

Third-party links are reported separately as UNVERIFIED rather than broken, because a bot
block is not evidence the link is dead for a human.

Run:  python3 projects/sagamore/tools/verify-broken-links.py
"""

import html
import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

BUILD = Path(__file__).resolve().parent.parent / "build"
REPORT = BUILD / "link-report.json"
OUT = BUILD / "broken-links-verified.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def probe(url, attempts=3):
    """Return (status, final_url). Retries, because a transient 0 is not a dead link."""
    last = 0
    for i in range(attempts):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        })
        try:
            with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
                return r.getcode(), r.geturl()
        except urllib.error.HTTPError as e:
            return e.code, url
        except Exception:
            last = 0
            time.sleep(1.5 * (i + 1))
    return last, url


def main():
    data = json.loads(REPORT.read_text())
    links = data["links"]

    suspects = {}
    for raw, rec in links.items():
        url = html.unescape(raw)
        if rec["status"] == 0 or rec["status"] >= 400:
            suspects[url] = rec["found_on"]

    council = {u: v for u, v in suspects.items() if "sagamorebsa.org" in urllib.parse.urlparse(u).netloc}
    third = {u: v for u, v in suspects.items() if u not in council}

    print(f"re-checking {len(council)} council-owned suspects, sequentially…\n")
    confirmed, recovered = {}, {}
    for i, (url, found_on) in enumerate(sorted(council.items()), 1):
        status, final = probe(url)
        if status == 0 or status >= 400:
            confirmed[url] = {"status": status, "found_on": found_on}
            mark = "BROKEN"
        else:
            recovered[url] = status
            mark = "ok"
        print(f"  [{i:>3}/{len(council)}] {mark:>6} {status:>3}  {url[:88]}")
        time.sleep(0.35)

    # Group the confirmed breaks into the patterns that actually matter.
    groups = defaultdict(list)
    for url in confirmed:
        p = urllib.parse.urlparse(url).path
        if p.startswith("/162"):
            groups["legacy /162 camp-reservation system"].append(url)
        elif not p.startswith("/htdocs/wordpress"):
            groups["written against the bare domain, missing /htdocs/wordpress"].append(url)
        else:
            groups["other"].append(url)

    OUT.write_text(json.dumps({
        "confirmed_broken": confirmed,
        "recovered_on_retry": recovered,
        "third_party_unverified": {u: links.get(u, {}).get("status") for u in third},
        "groups": {k: sorted(v) for k, v in groups.items()},
    }, indent=2))

    print(f"\n{'='*70}")
    print(f"CONFIRMED broken on the council's own domain : {len(confirmed)}")
    print(f"Recovered on retry (first pass was wrong)    : {len(recovered)}")
    print(f"Third-party, blocked us, NOT verified broken : {len(third)}")
    print(f"\nPatterns:")
    for name, urls in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(urls):>3}  {name}")
        for u in sorted(urls)[:4]:
            print(f"         {u}")
        if len(urls) > 4:
            print(f"         … and {len(urls)-4} more")
    print(f"\n-> {OUT}")


if __name__ == "__main__":
    main()
