# This script is not working for some reason
import scrapy # ignore this warning
import os
import sqlite3

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = "cve_persist_sql"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [f"file://{url}"] # this will do the job in case of the local file

    def parse(self, response):
        connection = sqlite3.connect('vuln.db')
        sql_table = "CREATE TABLE vuln (exploit TEXT, cve TEXT)"
        cursor = connection.cursor()
        cursor.execute(sql_table)
        connection.commit()
        for table in response.xpath('//table'):
            if len(table.xpath('tr')) > 100:
                break
        count = 0
        for row in table.xpath('//tr'):
            if count > 100:
                break
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                cursor.execute('INSERT INTO vuln (exploit, cve) VALUES(?, ?)', (exploit_id, cve_id))
                connection.commit()
                count +=1
            except IndexError:
                pass
            connection.close()


