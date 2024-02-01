# NOT WORKING
import scrapy
import os
import sqlite3

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = "cve_persist_sql"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [f"file://{url}"] 

    def parse(self, response):
        connection = sqlite3.connect('vuln.db')
        cursor = connection.cursor()
        tab_creat_query = "CREATE TABLE vuln (exploit TEXT, cve TEXT)"
        cursor.execute(tab_creat_query)
        connection.commit()
        for table in response.xpath('//table'):
            if len(table.xpath('tr')) > 100:
                break
        count = 0
        for row in table.xpath('//tr'):
            if count > 100:
                connection.close()
                break
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                insert_query = 'INSERT INTO vuln (exploit, cve) VALUES(?, ?)'
                cursor.execute(insert_query, [exploit_id, cve_id])
                connection.commit()
                count +=1
            except IndexError:
                pass