# 🌍 Country Information Explorer

A browser-based UI + Python CLI to explore country data from the [REST Countries API](https://restcountries.com).

## Screenshot

![UI Screenshot](screenshot.png)

## Features

| Feature | Browser UI | Python CLI |
|---|---|---|
| Search by name | ✅ | ✅ |
| Browse by region | ✅ | ✅ |
| Random country | ✅ | — |
| Flag display | ✅ | — |
| Population | ✅ | ✅ |
| Capital | ✅ | ✅ |
| Currency | ✅ | ✅ |
| Languages | ✅ | ✅ |
| Maps (Google + OSM) | ✅ | ✅ |
| Coat of Arms | ✅ | ✅ |
| Area / Timezone | ✅ | ✅ |

## Project Structure

```
country-explorer/
├── index.html          ← Browser UI (open directly, no server needed)
├── fetch_country.py    ← Python CLI script
├── README.md
└── screenshot.png
```

## Quick Start

### Browser UI
Just open `index.html` in any browser — no server, no install needed.

### Python CLI

No external dependencies — uses Python standard library only.

```bash
# List all countries
python3 fetch_country.py all

# Search by name
python3 fetch_country.py name "Germany"
python3 fetch_country.py name "ind"

# Lookup by ISO code (alpha-2 or alpha-3)
python3 fetch_country.py code IN
python3 fetch_country.py code USA
python3 fetch_country.py code DEU

# All countries in a region
python3 fetch_country.py region Asia
python3 fetch_country.py region Europe
python3 fetch_country.py region Africa
```

Output is JSON — pipe through `jq` for pretty formatting:

```bash
python3 fetch_country.py code JP | jq '.[] | {name: .name.common, capital: .capital, pop: .population}'
```

## API Used

- **Endpoint**: `https://restcountries.com/v3.1`
- **Auth**: None (free, public)
- **Docs**: https://restcountries.com

### Key endpoints used

| Endpoint | Purpose |
|---|---|
| `/all` | All countries |
| `/name/{name}` | Search by name |
| `/alpha/{code}` | Lookup by ISO code |
| `/region/{region}` | Filter by region |

## What I Learned

- How to make REST API calls from Python (`urllib`) and from the browser (`fetch`)
- How to parse and display JSON data dynamically in the DOM
- How to build a responsive, interactive browser UI with vanilla JS
- API field filtering (using `?fields=`) to reduce payload size
- Chaining async/await calls for a smooth UX

## Requirements

- Python 3.6+ (standard library only)
- Any modern browser for the UI
