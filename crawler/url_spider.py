import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sqlalchemy import func, create_engine, insert, select
from sqlalchemy.sql import func
from Model import page_table

class UrlSpiderSpider(CrawlSpider):
    name = "url_spider"
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir"]
    le1 = LinkExtractor()
    rules = (Rule(le1, callback="parse_item", follow=True),)

    def parse_item(self, response):
        items = response.xpath('//text()').getall()
        for i in items:
            yield{
                # 'text': items,
                'url': response.url
            }
            self.insert_db(1,2,3,1)
            print("ok")
            
    # insert data to pages table
    def insert_db(url, path, html, text):
      engine = create_engine("postgresql://postgres:1@db:5432/website_content")
      stmt = insert(page_table).values(url="url", path="path", html="html", text="text")
      with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
              

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(UrlSpiderSpider)
    process.start()