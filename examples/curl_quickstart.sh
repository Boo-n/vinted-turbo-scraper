#!/bin/bash
# Vinted Turbo Scraper — Quick cURL Example
# Replace YOUR_API_TOKEN below

curl -X POST "https://api.apify.com/v2/acts/kazkn~vinted-turbo-scraper/runs" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "searchURLs": [
      "https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=100"
    ],
    "maxItems": 100
  }'

# Then poll for results:
# GET https://api.apify.com/v2/acts/kazkn~vinted-turbo-scraper/runs/{runId}/dataset/items
