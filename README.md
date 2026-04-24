# ⚡ Vinted Turbo Scraper

Paste a filtered Vinted search URL, run, and export listings in seconds.

[![Apify Store](https://img.shields.io/badge/Apify%20Store-⚡%20Turbo%20Scraper-66fcf1?style=flat-square&logo=apify)](https://apify.com/kazkn/vinted-turbo-scraper)
[![GitHub issues](https://img.shields.io/github/issues/Boo-n/vinted-turbo-scraper?style=flat-square)](https://github.com/Boo-n/vinted-turbo-scraper/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 🔍 What It Does

**Vinted Turbo Scraper** turns existing Vinted search URLs into structured data as fast as possible.

Instead of manually rebuilding filters inside an input form, you simply:
1. Open a Vinted search page
2. Apply filters directly on Vinted
3. Copy the URL
4. Paste it into the actor
5. Export results as JSON, CSV, or Excel

### Data Extracted

| Field | Description |
|-------|-------------|
| `title` | Item title and description |
| `price` | Price and currency |
| `condition` | Item condition and category |
| `size` | Size, brand, and color |
| `images` | URLs to full HD photos |
| `seller_username` | Seller name and profile URL |
| `location` | Item location and shipping details |
| `item_status` | Available, sold, reserved |
| `scraped_at` | Exact ISO timestamp |
| `source_url` | The search URL that produced this result |

---

## 🎯 Who Is This For?

- 👟 **Resellers** who want fast listing extraction from filtered Vinted searches
- 📊 **Researchers and analysts** building datasets from Vinted catalog pages
- 🤖 **Automation builders** who want lightweight Vinted scraping in Apify workflows
- 🏪 **Operators monitoring** categories, brands, sizes, or price ranges with minimal setup

---

## ⚡ Why Use Vinted Turbo Scraper?

- **⚡ Fastest setup**: copy a Vinted URL and run immediately
- **🔗 URL-native workflow**: your filters already live inside the Vinted search URL
- **📦 Structured export**: JSON, CSV, Excel-ready output
- **🔁 Batch multiple URLs** in one run
- **🛠️ Great for monitoring** repeated searches, categories, and filtered product sets
- **🌍 26 Vinted country domains** supported

> 💡 If you want the most complete Vinted intelligence workflow with seller analysis, sold items, trending, and cross-country arbitrage, use [Vinted Smart Scraper](https://apify.com/kazkn/vinted-smart-scraper). If you want the fastest path from search URL to dataset, use Turbo.

---

## 🎬 Video Tutorial — See It in Action

- 🇬🇧 [English Tutorial](https://youtu.be/rWtZVDMflbo)
- 🇫🇷 [Tutoriel Français](https://youtu.be/IsQkno013mY)

---

## 🚀 Quick Start

Scraping Vinted with Vinted Turbo Scraper takes **less than a minute**:

1. Go to [vinted.com](https://www.vinted.com), apply your filters (brand, size, condition, price…) and **copy the search URL**
2. Paste one or multiple **Vinted search URLs** into the actor input
3. Click **Run**
4. Export the results as **JSON, CSV, Excel, or Google Sheets**

### Example JSON Output

```json
{
  "url": "https://www.vinted.fr/items/123456789-jordan-1-mid-chicago",
  "title": "Jordan 1 Mid 'Chicago'",
  "price": 75.00,
  "currency": "EUR",
  "brand": "Jordan",
  "size": "44",
  "condition": "Very good",
  "description": "Barely worn. No creases.",
  "seller_username": "sneakerhead_paris",
  "seller_url": "https://www.vinted.fr/member/987654321-sneakerhead_paris",
  "location": "Paris, France",
  "status": "available",
  "source_url": "https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=80",
  "thumbnail": "https://images1.vinted.net/t/01_01234abc.jpg",
  "images": [
    "https://images1.vinted.net/...",
    "https://images2.vinted.net/..."
  ],
  "scraped_at": "2026-04-24T10:15:30.000Z"
}
```

---

## 📖 Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `searchURLs` | String[] | ✅ | One or more Vinted search URLs to scrape |
| `maxItems` | Integer | ❌ | Maximum number of listings to extract per URL (default: unlimited) |
| `proxyConfiguration` | Object | ❌ | Custom proxy settings (auto-managed by default) |

### Batch URL Example

```json
{
  "searchURLs": [
    "https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=100",
    "https://www.vinted.de/catalog?search_text=jordan&price_from=40&price_to=90",
    "https://www.vinted.nl/catalog?search_text=nike&price_from=35&price_to=85"
  ]
}
```

---

## 💰 Pricing

**$0.0015 per result** ($1.50 per 1,000 listings scraped)

With Apify's free $5 monthly Platform Credits, you can scrape roughly **3,300 listings at zero cost**.

| Scenario | URLs | Results | Cost |
|----------|------|---------|------|
| Single search | 1 | ~500 | $0.75 |
| Small batch | 3 | ~1,200 | $1.80 |
| Medium batch | 10 | ~3,500 | $5.25 |
| Large batch | 15 | ~4,500 | $6.75 |

---

## 🔌 API & Integrations

### Using the API

**Python:**
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_API_TOKEN")
run = client.actor("kazkn/vinted-turbo-scraper").call(run_input={
    "searchURLs": ["https://www.vinted.fr/catalog?search_text=jordan"]
})

for item in client.dataset(run["defaultDatasetId"]).list_items():
    print(item["title"], item["price"])
```

**Node.js:**
```javascript
const { ApifyClient } = require('apify-client');
const client = new ApifyClient({ token: 'YOUR_API_TOKEN' });

const run = await client.actor('kazkn/vinted-turbo-scraper').call({
  searchURLs: ['https://www.vinted.fr/catalog?search_text=jordan'],
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

**cURL:**
```bash
curl -X POST "https://api.apify.com/v2/acts/kazkn~vinted-turbo-scraper/runs" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchURLs":["https://www.vinted.fr/catalog?search_text=jordan"]}'
```

### Integrations

- **n8n** — Trigger scrapes and push results to Telegram/Discord/Slack
- **Make.com (Integromat)** — Connect Vinted data to Google Sheets, Airtable, Notion
- **Zapier** — Build automated workflows on new listings

---

## 📚 Resources & Documentation

- 📖 [Apify Store Page](https://apify.com/kazkn/vinted-turbo-scraper)
- 📖 [API Documentation](https://apify.com/kazkn/vinted-turbo-scraper/api)
- 📖 [Python API Guide](https://apify.com/kazkn/vinted-turbo-scraper/api/python)
- 🌐 [Resources Hub](https://boo-n.github.io/vinted-turbo-scraper-hub/) — All tutorials, videos & guides

### Written Tutorials

- [How I Scrape 1,000 Vinted Listings in Under 2 Minutes](https://dev.to/boo_n/how-i-scrape-1000-vinted-listings-in-under-2-minutes-without-writing-a-single-line-of-code-1lol) — Dev.to
- [How to Batch-Scrape 10 Vinted Search URLs in One Run](https://dev.to/boo_n/how-to-batch-scrape-10-vinted-search-urls-in-one-run-a-resellers-workflow-4ed1) — Dev.to

### Related Actors

- [Vinted Smart Scraper](https://apify.com/kazkn/vinted-smart-scraper) — Cross-country price comparison, seller analysis, trending
- [Vinted MCP Server](https://apify.com/kazkn/vinted-mcp-server) — Natural language Vinted queries via Claude/Cursor

---

## ❓ FAQ

**Q: Is this legal?**
> We only extract publicly visible listing data — the same information any visitor sees on a Vinted search page. No private messages, no login-required data, no PII.

**Q: Will I get IP-banned?**
> The Actor runs on Apify's infrastructure with residential proxy rotation. In extensive testing we maintained a >90% success rate. Failed runs are retried automatically.

**Q: Can I schedule recurring runs?**
> Yes. Apify's scheduler lets you set up daily/hourly runs with push to Google Sheets, webhooks, or API.

**Q: What countries are supported?**
> All 26 Vinted country domains: France, Germany, Netherlands, Poland, Spain, Italy, UK, Belgium, Czech Republic, Austria, Portugal, Lithuania, Luxembourg, Slovakia, Hungary, Romania, Bulgaria, Greece, Croatia, Ireland, Latvia, Estonia, Finland, Sweden, Denmark, Norway.

**Q: What's the difference between Turbo and Smart Scraper?**
> **Turbo** = fastest, URL-based, single-country, structured export. **Smart** = deep analytics, cross-country comparison, seller intelligence, trending products.

---

## 🤝 Support

- [Open an issue](https://github.com/Boo-n/vinted-turbo-scraper/issues) on this repo
- [DM on X](https://twitter.com/DataKazKN)

---

**Built by [KazKN](https://apify.com/kazkn)**
