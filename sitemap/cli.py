import argparse
import asyncio
from .core import SiteMap
import json

def main():
    parser = argparse.ArgumentParser(
        prog="sitemap-cli",
        description="⚡ High-performance async sitemap URL extractor",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example: sitemap-cli https://site.com --filter news --output urls.jsonl",
    )

    parser.add_argument("url", help="Website or sitemap URL")

    parser.add_argument(
        "--filter",
        help="Only keep URLs containing this path segment/string",
    )

    parser.add_argument(
        "--output",
        help="Save results to JSONL file",
    )

    parser.add_argument(
        "--concurrency",
        type=int,
        default=10,
        help="Number of concurrent requests",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Request timeout in seconds",
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Print only URLs (no stats)",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="sitemap-cli 1.0",
    )

    args = parser.parse_args()

    # If the user requested a .jsonl output file, pass it to SiteMap so
    # the crawler can save one-URL-per-line format. Otherwise write a
    # normal JSON array to the provided filename.
    save_path = args.output if args.output and args.output.endswith(".jsonl") else None

    crawler = SiteMap(
        args.url,
        filter_pattern=args.filter,
        concurrency=args.concurrency,
        timeout=args.timeout,
        save=save_path,
    )

    urls, stats = asyncio.run(crawler.fetch())

    # If JSONL was requested, let the crawler write it.
    if args.output and args.output.endswith(".jsonl"):
        crawler.save_jsonl(urls=urls)
    elif args.output:
        with open(args.output, "w") as f:
            json.dump(list(urls), f, indent=2)

    if args.quiet:
        for u in urls:
            print(u)
    else:
        print("\n=== Results ===")
        print(f"URLs        : {stats.urls}")
        print(f"Sitemaps    : {stats.sitemaps}")
        print(f"Errors      : {stats.errors}")
        print(f"Rate        : {stats.rate():.2f} URLs/sec")
        print(f"Elapsed     : {stats.elapsed():.2f}s")