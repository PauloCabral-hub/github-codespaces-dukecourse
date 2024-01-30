import scrapy # try to solve this


class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        # you should reproduce here what you have seen in scrapy_shell_orientation,
        # the response here is the same. Attention, for some reason, scrapy command
        # craw is not available in the current version of the package.
        pass
