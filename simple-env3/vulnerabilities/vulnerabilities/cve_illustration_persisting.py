# This file does not run
# It is only made to follow the class since there is something new in scrapy tool
# that is not making it possible to work as it should
import scrapy # try to solve this
import os
from os.path import dirname

current_dir = dirname(__file__)
url = os.path.join(current_dir, '<HTML file downloaded and placed in this directory>')

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    #start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        # you should reproduce here what you have seen in scrapy_shell_orientation,
        # the response here is the same. Attention, for some reason, scrapy command
        # craw is not available in the current version of the package.
        pass
