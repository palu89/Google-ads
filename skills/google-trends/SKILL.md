# Google Trends Monitoring

Monitor and analyze Google Trends data for market research, content planning, and trend tracking.

## Capabilities

1. **Daily Trending Searches** - What's trending today in any country
2. **Keyword Interest Over Time** - Historical trend data for keywords
3. **Keyword Comparison** - Compare multiple keywords
4. **Related Topics & Queries** - Discover related searches
5. **Regional Interest** - See where keywords are most popular

## Usage (CLI / Terminal)

### Get Trending Searches (Today)
```bash
# Example: US Daily Trends
curl -s "https://trends.google.com/trending/rss?geo=US" | grep -o '<title>[^<]*</title>' | sed 's/<[^>]*>//g' | tail -n +2 | head -20
```

### Check Keyword Interest (Open Browser)
```bash
# Open comparison in browser
open "https://trends.google.com/trends/explore?q=bitcoin,ethereum,solana&geo=US"
```

## Integration with Google Ads
Use this skill when:
- Researching new markets (e.g., Japan)
- Identifying seasonal spikes for budget pacing
- Finding negative keyword candidates from unrelated "trending" topics
