# 🎭 Google Events API: Event Search in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Events API.

**Actor page:** [apify.com/johnvc/google-events-api---access-google-events-data](https://apify.com/johnvc/google-events-api---access-google-events-data?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-events-api---access-google-events-data/input-schema](https://apify.com/johnvc/google-events-api---access-google-events-data/input-schema?fpr=9n7kx3)

The Google Events API runs an event search for any query and returns clean, structured JSON. Each page of results comes back with event titles and descriptions, dates and full date/time ranges, venue names with ratings and reviews, multi-line addresses, ticket-provider links (Ticketmaster, Eventbrite, Spotify, and more), map preview images and links, and the filter chips Google offers. It supports location biasing, country and language localization, date and event-type filters, and pagination.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Events-API.git
   cd Apify-Google-Events-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-events-api.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-events-api.py
```

## Why Use This Google Events API?

**Full event detail.** Each result includes the title, description, dates, venue (with rating and reviews), address, ticket links from multiple providers, and map links, so you get everything Google Events shows in one structured record.

**Aggregated ticket links.** Ticket sources like Ticketmaster, Eventbrite, Spotify, AXS, and SeatGeek are collected per event, ready to surface purchase options.

**Localized and filterable.** Bias by location, localize by country and language (240+ countries, 200+ languages), and filter with Google's own chips: date (today, this week, weekend, month) and event type (virtual).

**Predictable, pay-per-use pricing.** Billing is per run plus per page processed, with no subscription. You control cost with the page limit.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can find events for you on demand.

## Features

### Core Capabilities
- **Natural-language event search** across concerts, conferences, festivals, sports, theater, and virtual events
- **Location biasing** plus country (`gl`) and language (`hl`) localization
- **Date and event-type filters** via Google's hit chips
- **Multi-page pagination** with a configurable page cap

### Data Quality
- **Structured events** with title, description, dates, address, and primary link
- **Ticket links** aggregated from multiple providers
- **Venue details** with name, rating, and review count
- **Map previews** (image and Google Maps link) per event
- **Per-page metadata** and consistent JSON across queries

## Usage Examples

### Basic search
```json
{
  "q": "concerts in New York",
  "max_pages": 1
}
```

### Localized search
```json
{
  "q": "music festivals",
  "location": "Austin, Texas, United States",
  "gl": "us",
  "hl": "en",
  "max_pages": 2
}
```

### Today's virtual events (filter chips)
```json
{
  "q": "tech conferences",
  "advanced": "event_type:Virtual-Event,date:today",
  "max_pages": 1
}
```

The `advanced` parameter accepts Google's filter chips: `date:today`, `date:tomorrow`, `date:week`, `date:weekend`, `date:next_week`, `date:month`, `date:next_month`, and `event_type:Virtual-Event`. Pass one token, a comma-separated string, or an array.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `string` | Yes | - | Event search query, e.g. `concerts in New York`, `tech conferences this week`. |
| `location` | `string` | No | (none) | Geographic location to bias results, e.g. `Austin, Texas, United States`. |
| `gl` | `string` | No | (none) | Country code (ISO 3166-1 alpha-2, lowercase). 240+ supported. |
| `hl` | `string` | No | (none) | Language code (ISO 639-1, lowercase). 200+ supported. |
| `advanced` | `string` or `array` | No | (none) | Filter chips: `date:*` and `event_type:Virtual-Event`. |
| `max_pages` | `integer` | No | `1` | Maximum pages to fetch (`0` = no limit). Each page is billed separately. |
| `output_file` | `string` | No | (none) | Optional filename to save results. |

## Output Format

A real result for `concerts in New York` (one item per page; the event description, map URLs, and the date range label are trimmed here for readability).

```json
{
  "search_parameters": {
    "q": "concerts in New York",
    "location": "New York, NY",
    "gl": "us",
    "hl": "en",
    "max_pages": 1
  },
  "search_metadata": {
    "total_results": 10,
    "events_count": 10,
    "hit_chips_count": 0,
    "filters_count": 0,
    "pages_processed": 1,
    "max_pages_set": 1,
    "pagination_limit_reached": true
  },
  "search_timestamp": "2026-05-29T10:43:56",
  "page_number": 1,
  "events": [
    {
      "title": "O-Zone Concert in New York",
      "date": {
        "start_date": "May 31",
        "when": "Sun, May 31 - Mon, Jun 1"
      },
      "address": [
        "Melrose Ballroom, 36-08 33rd St",
        "Long Island City, NY"
      ],
      "link": "https://www.melroseballroom.com/events/o-zone-concert-in-new-york",
      "description": "The legendary group O-Zone is coming to the United States for the very first time.",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=...",
        "link": "https://www.google.com/maps/place/..."
      },
      "ticket_info": [
        { "source": "melroseballroom.com", "link": "https://www.melroseballroom.com/...", "link_type": "tickets" }
      ],
      "venue": {}
    }
  ],
  "hit_chips": [],
  "filters": []
}
```

---

## Use as an MCP tool

You can load the Google Events API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Events API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Events API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Events API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-events-api---access-google-events-data`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data`, using OAuth when prompted.
5. Ask Claude to run the Google Events API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Events API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-events-api---access-google-events-data`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Events API to power event discovery, calendars, and market research with reliable, structured results.*

Last Updated: 2026.06.11
