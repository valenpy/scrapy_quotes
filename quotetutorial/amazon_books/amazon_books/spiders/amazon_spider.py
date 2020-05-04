import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'
    ]

    def parse(self, response):
        book_titles = response.css('span.a-text-normal::text').extract()
        xpath = response.xpath('//title/text()').extract()  # 'xpath': ['<title>Amazon.com: Last 30 days: Books</title>']}
        yield {'book_titles': book_titles, 'xpath': xpath}

