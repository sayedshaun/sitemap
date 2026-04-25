# sitemap

Async sitemap crawler with an easy CLI and Python API.

**Features**
- **Async**: built with `aiohttp` and `asyncio` for efficient concurrent fetching.
- **Sitemap-aware**: understands sitemap index and URL sets.
- **Filterable**: pass a substring to include only matching URLs.
- **CLI + Library**: use the `sitemap-cli` command or import `SiteMap` in Python.

**Install**

Install into your active virtualenv (editable mode recommended during development):

```bash
python -m pip install -e .
```

Or install from PyPI (when published):

```bash
python -m pip install sitemap
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

**Project layout**

- `sitemap/cli.py` — CLI entrypoint and argument parsing.
- `sitemap/core.py` — `SiteMap` crawler implementation.
- `pyproject.toml` — package metadata and console script entry.

See the `pyproject.toml` for the console script `sitemap-cli`.

**Contributing**

Contributions, issues, and improvements are welcome. Please open a GitHub issue or PR.

**License**

MIT — see LICENSE for details.
