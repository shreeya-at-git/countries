#!/usr/bin/env python3
"""
Country Information Explorer
Uses the REST Countries API (https://restcountries.com) to fetch country details.
"""

import sys
import json
import urllib.request
import urllib.parse
import urllib.error

BASE_URL = "https://restcountries.com/v3.1"

FIELDS = "name,capital,population,currencies,flags,maps,region,subregion,languages,area,timezones,continents,coatOfArms"


def fetch_all_countries():
    """Fetch a summary list of all countries."""
    url = f"{BASE_URL}/all?fields=name,flags,region,population,capital"
    return _get(url)


def fetch_by_name(name: str):
    """Search countries by name (common or official)."""
    encoded = urllib.parse.quote(name)
    url = f"{BASE_URL}/name/{encoded}?fields={FIELDS}"
    return _get(url)


def fetch_by_code(code: str):
    """Fetch a single country by ISO alpha-2 or alpha-3 code."""
    encoded = urllib.parse.quote(code.upper())
    url = f"{BASE_URL}/alpha/{encoded}?fields={FIELDS}"
    return _get(url)


def fetch_by_region(region: str):
    """Fetch all countries in a given region."""
    encoded = urllib.parse.quote(region)
    url = f"{BASE_URL}/region/{encoded}?fields={FIELDS}"
    return _get(url)


def _get(url: str):
    """Internal HTTP GET helper; returns parsed JSON or raises."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code}: {exc.reason}  →  {url}", file=sys.stderr)
        return None
    except urllib.error.URLError as exc:
        print(f"Network error: {exc.reason}", file=sys.stderr)
        return None


def pretty(data):
    """Pretty-print JSON to stdout."""
    print(json.dumps(data, indent=2, ensure_ascii=False))


# ── CLI entry point ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch country data from the REST Countries API."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_all = sub.add_parser("all", help="List all countries (name, flag, region, population, capital)")
    p_name = sub.add_parser("name", help="Search by country name")
    p_name.add_argument("query", help="Full or partial country name")
    p_code = sub.add_parser("code", help="Lookup by ISO alpha-2/3 code")
    p_code.add_argument("code", help="e.g. IN, USA, DEU")
    p_region = sub.add_parser("region", help="All countries in a region")
    p_region.add_argument("region", help="Africa | Americas | Asia | Europe | Oceania")

    args = parser.parse_args()

    if args.cmd == "all":
        data = fetch_all_countries()
    elif args.cmd == "name":
        data = fetch_by_name(args.query)
    elif args.cmd == "code":
        data = fetch_by_code(args.code)
    elif args.cmd == "region":
        data = fetch_by_region(args.region)

    if data:
        pretty(data)
    else:
        sys.exit(1)