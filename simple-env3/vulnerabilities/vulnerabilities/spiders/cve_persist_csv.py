import scrapy # ignore this warning
import os
import csv

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = "cve_persist_csv"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [f"file://{url}"] # this will do the job in case of the local file

    def parse(self, response):
        for table in response.xpath('//table'):
            if len(table.xpath('tr')) > 100:
                break
        count = 0
        csv_file = open('vulnerabilites.csv','w')
        writer = csv.writer(csv_file)
        writer.writerow(['exploit_id','cve_id'])
        for row in table.xpath('//tr'):
            if count > 100:
                break
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                writer.writerow([exploit_id, cve_id])
                count +=1
            except IndexError:
                pass
        csv_file.close()

