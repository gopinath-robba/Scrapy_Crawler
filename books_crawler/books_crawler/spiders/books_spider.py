import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['https://books.toscrape.com/']

    custom_settings = {
        'DEPTH_LIMIT': 3,  # Adjust the maximum depth of crawling
        'CLOSESPIDER_PAGECOUNT': 100,  # Adjust the maximum number of pages to crawl
    }

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'books-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Follow links to next pages within the domain
        for next_page in response.css('a::attr(href)'):
            if next_page is not None:
                yield response.follow(next_page, self.parse)
