"""
Vinted Turbo Scraper — Python API Example (Batch URLs)
Monitor multiple brands/countries in a single run.
Requires: pip install apify-client
"""
from apify_client import ApifyClient
import json

client = ApifyClient("YOUR_API_TOKEN")

# Multiple search URLs — different brands, same country
run_input = {
    "searchURLs": [
        # Jordan in France
        "https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=100",
        # Nike in France
        "https://www.vinted.fr/catalog?search_text=nike&price_from=30&price_to=80",
        # Jordan in Germany
        "https://www.vinted.de/catalog?search_text=jordan&price_from=40&price_to=90",
        # Nike in Netherlands
        "https://www.vinted.nl/catalog?search_text=nike&price_from=35&price_to=85"
    ],
    "maxItems": 1000
}

print(f"Batching {len(run_input['searchURLs'])} URLs...")
run = client.actor("kazkn/vinted-turbo-scraper").call(run_input=run_input)

# Results merged in one dataset
items = client.dataset(run["defaultDatasetId"]).list_items().items

# Segment by source_url
by_source = {}
for item in items:
    src = item.get("source_url", "unknown")
    by_source.setdefault(src, []).append(item)

for url, listings in by_source.items():
    print(f"\n{url}: {len(listings)} results")
    for l in listings[:3]:
        print(f"  {l['title']} | {l['price']} | {l['size']}")
