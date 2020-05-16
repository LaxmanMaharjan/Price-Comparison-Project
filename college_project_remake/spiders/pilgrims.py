import scrapy

from college_project_remake.items import CollegeProjectRemakeItem
from college_project_remake.Controller import book_name
class PilgrimsSpider(scrapy.Spider):
    name = 'pilgrims'
    #book_name = "palpasa cafe"
    allowed_domains = ['pilgrimsonlineshop.com']
    start_urls = [f'https://www.pilgrimsonlineshop.com/search?q={book_name}']

    def parse(self, response):
        items = CollegeProjectRemakeItem()
        result_books = response.xpath(
            "//div[@class='book-list']/ul/li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-2']/div[@class='zoom']")

        for book in result_books:
            price = book.xpath(".//div[@class='caption']/p/span/text()").get()
            managed_price = price[4:]
            new_price = float(managed_price) * 100
            new_price = int(new_price)

            items['Name']= book.xpath(".//div[@class='caption']/h4/a/text()").get()
            items['Book_link']= book.xpath(".//a/@href").get()
            items['Img_link']= book.xpath(".//a/img/@src").get()
            items['Price'] =str(new_price)
                # 'No_discounted_Price': book.xpath(
                #     "normalize-space(.//a/div/div[@class='panel-footer']/small/text()[2])").get()
            yield items
           # yield {'User-Agent':response.request.headers.get('User-Agent')}