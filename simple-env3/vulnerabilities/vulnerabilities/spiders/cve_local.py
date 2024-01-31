import scrapy # ignore this warning
import os

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = "cve_local"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [f"file://{url}"] # this will do the job in case of the local file

    def parse(self, response):
        for table in response.xpath('//table'):
            if len(table.xpath('tr')) > 100:
                break
        
        for row in table.xpath('//tr'):
            try:
                print(row.xpath('td//text()')[0].extract())
            except IndexError:
                pass

