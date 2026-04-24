"""
Vinted Turbo Scraper — Python API Example (Single URL)
Requires: pip install apify-client
"""
from apify_client import ApifyClient

# 1. Authenticate
client = ApifyClient("YOUR_API_TOKEN")

# 2. Configure run
run_input = {
    "searchURLs": [
        "https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=100&status_id=6"
    ],
    "maxItems": 500
}

# 3. Run actor
print("Running Vinted Turbo Scraper...")
run = client.actor("kazkn/vinted-turbo-scraper").call(run_input=run_input)

# 4. Fetch results
print(f"Dataset ID: {run['defaultDatasetId']}")
dataset = client.dataset(run["defaultDatasetId"])
items = dataset.list_items().items

print(f"Scraped {len(items)} listings")
for item in items[:5]:
    print(f"  {item['title']} — {item['price']} {item['currency']}")

# 5. Export to CSV manually (optional)
import csv
with open("vinted_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=items[0].keys())
    writer.writeheader()
    writer.writerows(items)
print("Saved to vinted_results.csv")
