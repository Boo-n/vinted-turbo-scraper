/**
 * Vinted Turbo Scraper — Node.js API Example
 * Requires: npm install apify-client
 */
const { ApifyClient } = require('apify-client');

const client = new ApifyClient({ token: 'YOUR_API_TOKEN' });

async function scrapeVinted() {
    const runInput = {
        searchURLs: [
            'https://www.vinted.fr/catalog?search_text=jordan&price_from=50&price_to=100&status_id=6'
        ],
        maxItems: 500
    };

    console.log('Running Vinted Turbo Scraper...');
    const run = await client.actor('kazkn/vinted-turbo-scraper').call(runInput);

    // Fetch dataset
    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    console.log(`Scraped ${items.length} listings`);

    // Pretty-print first 5
    items.slice(0, 5).forEach(item => {
        console.log(`  ${item.title} — ${item.price} ${item.currency}`);
    });

    return items;
}

scrapeVinted().catch(console.error);
