# firecrawl (Hermes Agent plugin)

Firecrawl web scraping and search plugin. Scrape URLs, crawl sites, search the web, map site structures, extract structured data, batch scraping, autonomous research agents, and cloud browser sessions via MCP tools.

## Install

Recommended (git-clone install, if this bundle is pushed to its own repo):

```bash
hermes plugins install <org>/firecrawl
```

Manual (flattened) install:

```bash
mkdir -p ~/.hermes/plugins/firecrawl
cp .hermes-plugin/plugin.yaml .hermes-plugin/__init__.py ~/.hermes/plugins/firecrawl/
cp -r skills ~/.hermes/plugins/firecrawl/
```

## Skills (7)

- `agent-research` — Autonomous research agent — start complex web research tasks, get structured results. This skill should be used when the user asks for multi-site exploration, open-ended web research, or deep-dive analysis across multiple sources.
- `batch-operations` — Batch scraping — scrape multiple URLs in a single request with rate limiting and progress tracking. This skill should be used when the user asks to scrape multiple pages at once, process a list of URLs, or bulk extract content.
- `browser-sessions` — Cloud browser sessions — create sessions, execute code, interact with dynamic pages. This skill should be used when the user needs to interact with SPAs, handle authentication flows, or execute browser automation on JavaScript-heavy sites.
- `crawling` — Multi-page crawling and site mapping. This skill should be used when the user asks to crawl an entire website, map all URLs on a site, discover site structure, or scrape multiple pages from a domain.
- `examples` — Tool call patterns, end-to-end workflow examples, and scenario references. This skill should be used when the user needs reference implementations, complete examples, or tool call patterns.
- `scraping` — Single URL scraping — formats, selectors, wait strategies, headers. This skill should be used when the user asks to scrape a web page, get content from a URL, convert a page to markdown, or extract text from a site.
- `search-extract` — Web search and structured data extraction. This skill should be used when the user asks to search the web, extract structured data from pages into JSON, research a topic using online sources, or perform competitive analysis.

## Not carried over

- 1 agent(s) — no Hermes manifest equivalent
- 7 command(s) — no Hermes manifest equivalent
- MCP servers — not generated for Hermes

## Source

Canonical: https://github.com/agents-store/claude-public-plugins/tree/main/plugins/firecrawl
