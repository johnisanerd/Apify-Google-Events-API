[https://apify.com/johnvc/google-events-api---access-google-events-data](https://apify.com/johnvc/google-events-api---access-google-events-data?fpr=9n7kx3)

# 🎭 Google Events API - Access Google Events Data

> **The most powerful, reliable, and feature-rich Google Events search scraper for Apify**

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Apify-Google-Events-API
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using UV (recommended)
   uv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Using UV (recommended)
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python google-events-api.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python google-events-api.py
```

## 🌟 Why Choose This Scraper?

The Google Events API delivers enterprise-grade performance with these advanced capabilities:

**Performance & Reliability**: Built optimized for high-throughput scraping with intelligent rate limiting and pagination handling.

**Cost-Effective**: Pay per event with transparent pricing. No hidden fees or monthly subscriptions. Pay only for what you use.

**Lightning-Fast Event Discovery**: Search any event query across Google Events with blazing-fast performance. Retrieve comprehensive event data in seconds, not minutes, with intelligent caching and optimization.

**Precision Targeting & Advanced Filtering**: Pinpoint exact event parameters with date ranges (today, tomorrow, week, month), event types (virtual events), location targeting, and localization support. Get precisely the event data you need, when you need it.

**Rich, Structured Data Extraction**: Extract complete event information, including event titles, descriptions, dates, times, locations, ticket information, venue details, and more. Our advanced parsing ensures you get clean, structured data ready for immediate use.

**Enterprise-Grade Configuration & Flexibility**: Built for developers and businesses who demand reliability. Highly configurable with intuitive controls, comprehensive error handling, and robust logging. Focus on your business logic while we handle the complexity of event scraping.

**No Hidden Costs or Rental Fees**: We do not charge monthly rentals, our scraper operates on a pay-per-event model. Scale up or down based on your actual needs without being locked into expensive subscriptions.

## 🚀 Features

### Core Capabilities
- **Advanced Search**: Support for complex queries with location targeting, localization, and advanced filters (hit chips)
- **Intelligent Pagination**: Automatic handling of Google Events pagination with configurable page limits
- **Date Filtering**: Filter events by date ranges (today, tomorrow, week, weekend, month)
- **Event Type Filtering**: Filter for virtual events using `event_type:Virtual-Event`
- **Multi-Language & Localization**: Support for international event markets with country and language options
- **Location Targeting**: Narrow down events to specific geographic areas

### Data Quality
- **Clean Output**: Automatic structured data metadata for clean, production-ready data
- **Structured Results**: Consistent JSON structure across all event results
- **Comprehensive Fields**: Event details, dates, locations, ticket information, venue details, and more
- **Metadata Tracking**: Search-level analytics and event performance metrics
- **Per-Page Billing**: Results are pushed as separate dataset items for accurate billing

## 📖 Usage Examples

### Example 1: Basic Search (Events in New York)

Search for events with a simple query.

```json
{
  "q": "events in New York",
  "max_pages": 1
}
```

### Example 2: Search with Location and Localization

Search for events with geographic location and language preferences.

```json
{
  "q": "concerts",
  "location": "Austin, Texas, United States",
  "gl": "us",
  "hl": "en",
  "max_pages": 1
}
```

### Example 3: Search with Single Hit Chip (String)

Search for today's events using a date filter.

```json
{
  "q": "sports events",
  "location": "Los Angeles, CA",
  "advanced": "date:today",
  "max_pages": 1
}
```

### Example 3b: Search with Comma-Separated Hit Chips (String)

Search for today's virtual events using multiple filters.

```json
{
  "q": "concerts",
  "advanced": "event_type:Virtual-Event,date:today",
  "max_pages": 1
}
```

### Example 3c: Search with List of Hit Chips

Search using a list of advanced filters.

```json
{
  "q": "conferences",
  "advanced": ["date:today", "event_type:Virtual-Event"],
  "max_pages": 2
}
```

### Example 4: Pagination (Multiple Pages)

Search across multiple pages to get more results.

```json
{
  "q": "music festivals",
  "location": "California, United States",
  "gl": "us",
  "hl": "en",
  "max_pages": 2
}
```

### Example 5: Comprehensive Search (All Parameters + Advanced Filters)

Search with all available parameters including location, localization, and advanced filters.

```json
{
  "q": "theater shows",
  "location": "New York, NY",
  "gl": "us",
  "hl": "en",
  "advanced": ["date:month", "event_type:Virtual-Event"],
  "max_pages": 2
}
```

## 🔍 Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `str` | ✅ **Yes** | - | Search query string (e.g., "concerts in New York", "sports events", "theater shows"). **Required.** |
| `location` | `str` | ❌ | - | Geographic location to narrow down events (e.g., "Austin, Texas, United States", "New York, NY", "Los Angeles, CA") |
| `gl` | `str` | ❌ | - | Country code for localization (e.g., "us", "uk", "ca", "au"). See Country Codes section below. |
| `hl` | `str` | ❌ | - | Language code for localization (e.g., "en", "es", "fr", "de"). See Language Codes section below. |
| `advanced` | `str` or `list[str]` | ❌ | - | Advanced filters (hit chips) as string, comma-separated string, or array. See Advanced Filters section below. |
| `max_pages` | `int` | ❌ | `1` | Maximum number of pages to fetch. Set to `0` for no limit (fetch all available pages). Each page is charged separately. |

### Advanced Filters (Hit Chips)

The `advanced` parameter accepts hit chips for filtering events. Available filters include:

#### Date Filters
- `date:today` - Events happening today
- `date:tomorrow` - Events happening tomorrow
- `date:week` - Events happening this week
- `date:weekend` - Events happening this weekend
- `date:month` - Events happening this month

#### Event Type Filters
- `event_type:Virtual-Event` - Filter for virtual/online events only

#### Usage Examples
- Single filter: `"advanced": "date:today"`
- Multiple filters (comma-separated): `"advanced": "event_type:Virtual-Event,date:today"`
- Multiple filters (array): `"advanced": ["date:today", "event_type:Virtual-Event"]`

### Country Codes (gl parameter)

Common country codes:
- `us` - United States
- `uk` - United Kingdom
- `ca` - Canada
- `au` - Australia
- `de` - Germany
- `fr` - France
- `es` - Spain
- `it` - Italy
- `jp` - Japan
- `cn` - China

### Language Codes (hl parameter)

Common language codes:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `zh` - Chinese
- `ja` - Japanese
- `ko` - Korean
- `ru` - Russian

## 📊 Output Format

### Event Result Structure

```json
{
  "events": [
    {
      "title": "Summer Music Festival",
      "description": "Join us for an amazing summer music festival...",
      "date": "2025-07-15",
      "time": "18:00",
      "when": "Saturday, July 15 at 6:00 PM",
      "location": "Central Park, New York, NY",
      "venue": {
        "name": "Central Park",
        "rating": 4.5,
        "reviews": 1234,
        "link": "https://maps.google.com/..."
      },
      "ticket_info": {
        "sources": [
          {
            "provider": "Ticketmaster",
            "link": "https://ticketmaster.com/..."
          },
          {
            "provider": "Eventbrite",
            "link": "https://eventbrite.com/..."
          }
        ]
      },
      "event_link": "https://example.com/event",
      "map_image": "https://maps.google.com/...",
      "map_link": "https://maps.google.com/..."
    }
  ],
  "search_metadata": {
    "query": "concerts",
    "location": "New York, NY",
    "gl": "us",
    "hl": "en",
    "max_pages": 2,
    "pages_processed": 2,
    "events_count": 25
  },
  "hit_chips": [
    "date:today",
    "date:week",
    "event_type:Virtual-Event"
  ]
}
```

### Data Fields Extracted

| Field | Description |
|-------|-------------|
| **Event Details** | Event title, description, dates, times, and links |
| **Date & Time Info** | Start dates, event duration, "when" descriptions |
| **Location Data** | Event addresses, venue information, location maps |
| **Ticket Information** | Ticket sources, links, ticket providers (Ticketmaster, Eventbrite, etc.) |
| **Venue Details** | Venue name, ratings, reviews, venue links |
| **Location Maps** | Map images and links to event locations |
| **Hit Chips** | Filter chips available in search results (date filters, event types) |
| **Search Filters** | Available filter options for refining searches |
| **Search Metadata** | Total results, pages processed, pagination info |

## 💡 Use Cases

* **Event Discovery Platforms**: Build event discovery platforms and aggregators
* **Data Analytics**: Collect event data for business intelligence and analysis
* **Event Planning**: Research events for personal or business planning
* **Lead Generation**: Identify popular events and trending venues for business opportunities
* **Content Creation**: Gather event data for content marketing and SEO
* **Virtual Event Discovery**: Find and track virtual/online events using `event_type:Virtual-Event` filter

## ❓ Frequently Asked Questions

### Q1. How do I get started with Google Events API?

Simply provide a `q` (search query) parameter with your search term, then run the Actor. The scraper will automatically extract event data and return structured JSON results.

### Q2. Is the search query (`q`) parameter required?

Yes, the `q` parameter is **required**. You must provide a search query to search for events.

### Q3. Can I filter results by date?

Yes! Use the `advanced` parameter with date filters like `date:today`, `date:week`, `date:month`, etc. See the **Advanced Filters (Hit Chips)** section above for all available date filters.

### Q4. How do I search for virtual events?

Use the `advanced` parameter with `event_type:Virtual-Event`. You can combine it with date filters: `"event_type:Virtual-Event,date:today"` to find today's virtual events.

### Q5. Can I use multiple filters at once?

Yes! You can combine multiple filters by:
- Using comma-separated string: `"event_type:Virtual-Event,date:today"`
- Using an array: `["date:today", "event_type:Virtual-Event"]`

### Q6. How does pagination work?

The scraper automatically handles pagination. Set `max_pages` to control how many pages to fetch:
- `max_pages: 1` (default) - Fetch only the first page
- `max_pages: 5` - Fetch up to 5 pages
- `max_pages: 0` - Fetch all available pages (no limit)

Each page is charged separately.

### Q7. Can I search in different countries and languages?

Yes! Use the `gl` (country code) and `hl` (language code) parameters for localization. See the **Country Codes** and **Language Codes** sections above for available options.

### Q8. What data format does the scraper return?

The scraper returns structured JSON data with event details, dates, locations, ticket information, and metadata. Results are automatically cleaned and validated for schema compliance.

### Q9. Can I export the data?

Yes! Results are stored in Apify's dataset format and can be exported as JSON, CSV, Excel, or accessed via API.

### Q10. How do I use the location parameter?

The `location` parameter helps narrow down events to a specific geographic area. Examples: `"Austin, Texas, United States"`, `"New York, NY"`, `"Los Angeles, CA"`.

### Q11. What happens if my search returns no results?

If a search returns no events, the `events_count` in `search_metadata` will be `0`, and the `events` array will be empty. The Actor will still complete successfully and return the search metadata.

## 📝 Technical Notes

* Results are sorted by relevance by default (Google Events API default)
* The `q` parameter is required and must be a non-empty string
* Date filters in `advanced` parameter use Google's predefined date ranges (today, week, month, etc.)
* Each page is pushed as a separate dataset item for accurate per-page billing
* Results are automatically cleaned and validated to ensure JSON-serializable output
* The `max_pages` parameter controls how many pages to fetch. Set to `0` for no limit (fetch all available pages)
* The `advanced` parameter accepts strings, comma-separated strings, or arrays of strings
* Location and localization parameters (`location`, `gl`, `hl`) are optional but recommended for better results
* Event data includes ticket information from multiple sources (Ticketmaster, Eventbrite, Spotify, etc.)
* Venue information includes ratings and reviews when available

## 🚀 Ready to Collect Google Events Data?

Start using Google Events API today and transform public event listings into actionable insights. Whether you're building event discovery platforms, monitoring event trends, conducting market research, or creating event aggregation applications, you'll have clean, structured data in minutes!

[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your event search automation with the most reliable and feature-rich Google Events scraper on Apify.*

Last Updated: 2025.11.17
