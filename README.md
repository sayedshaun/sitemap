# Sitemap

Async sitemap crawler with an easy CLI and Python API.

**Features**
- **Async**: built with `aiohttp` and `asyncio` for efficient concurrent fetching.
- **Sitemap-aware**: understands sitemap index and URL sets.
- **Filterable**: pass a substring to include only matching URLs.
- **CLI + Library**: use the `sitemap-cli` command or import `SiteMap` in Python.

**Install**

```bash
git clone https://github.com/sayedshaun/sitemap.git
cd sitemap
```

Then install with pip:
```bash
python -m pip install .
```

**Quick CLI Usage**

Basic usage:

```bash
sitemap-cli "https://example.com"
```

Save results to JSON (array):

```bash
sitemap-cli "https://example.com" --output urls.json
```

Filter URLs containing "blog" and save as JSONL (one URL per line):
```bash
sitemap-cli "https://example.com" --output urls.jsonl --filter "blog"
```

Quiet mode (print one URL per line):

```bash
sitemap-cli "https://example.com" --quiet
```

Useful options:
- `--filter`: only include URLs containing this substring.
- `--concurrency`: number of concurrent requests (default: 10).
- `--timeout`: request timeout in seconds (default: 10).

**Python API**

Import and use the `SiteMap` crawler directly:

```python
import asyncio
from sitemap import SiteMap

async def main():
    crawler = SiteMap("https://example.com", filter_pattern="blog", concurrency=10)
    urls, stats = await crawler.fetch()
    print(f"found {stats.urls} urls in {stats.elapsed():.2f}s")

asyncio.run(main())
```

Or use the synchronous helper:

```python
from sitemap import SiteMap

crawler = SiteMap("https://example.com")
urls, stats = crawler.run()
print(len(urls))
```

**Contributing**

Contributions, issues, and improvements are welcome. Please open a GitHub issue or PR.

**License** is licensed under the MIT License. See [LICENSE](LICENSE) for details.
