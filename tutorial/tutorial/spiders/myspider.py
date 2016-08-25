import scrapy
from scrapy.shell import inspect_response


class BlogSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.google.com.ua/search?q=useragent']

    def parse(self, response):
        # inspect_response(response, self)
        for item in response.css('#search h3 a'):
            yield {
                'text': item.xpath('text()').extract()[0],
                'url': item.xpath('@href').extract()[0],
            }
            # yield scrapy.Request(response.urljoin(url), self.parse_titles)
