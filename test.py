from sitemap import SiteMap

crawler = SiteMap("https://rumorscanner.com", save="output.jsonl", filter_pattern="fact-check")
urls, stats = crawler.run()

print(stats)