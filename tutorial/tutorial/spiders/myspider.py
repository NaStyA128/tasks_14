import scrapy
from scrapy.shell import inspect_response
from tutorial.items import TutorialItem


class BlogSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.google.com.ua/search?q=useragent&start=0',
                  'https://www.google.com.ua/search?q=useragent&start=10',
                  'https://www.google.com.ua/search?q=useragent&start=20']

    def parse(self, response):
        # inspect_response(response, self)
        # print(response.headers)

        for result_a in response.css('#search h3 a'):
            item = TutorialItem()
            item['url'] = result_a.xpath('@href').extract()[0]
            item['text_url'] = result_a.xpath('text()').extract()[0]
            yield item
            # yield {
            #     'text': item.xpath('text()').extract()[0],
            #     'url': item.xpath('@href').extract()[0],
            # }
            # yield scrapy.Request(response.urljoin(url), self.parse_titles)
