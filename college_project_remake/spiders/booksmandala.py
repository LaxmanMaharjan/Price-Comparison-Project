import scrapy

from college_project_remake.items import CollegeProjectRemakeItem
from college_project_remake.Controller import book_name
class BooksmandalaSpider(scrapy.Spider):
    name = 'booksmandala'
   # book_name = Controller.input_book_name()
    #book_name = "palpasa cafe"
    allowed_domains = ['booksmandala.com']
    start_urls = [f'https://booksmandala.com/search?name={book_name}']

    def parse(self, response):
        items = CollegeProjectRemakeItem()

        result_books = response.xpath("//div[@class='col-lg-9 col-sm-7']/div[@class='row mt-4 search-result']/div[@class='col-6 col-md-3']")

        for book in result_books:
            price = book.xpath(".//div/div/p/text()").get()
            managed_price = price[4:]
            new_price = str(managed_price)
            link = book.xpath(".//div/a/@href").get()
            absolute_url = response.urljoin(link)
            items['Name'] = book.xpath(".//div/div/h3/a/text()").get()
            items['Book_link']=absolute_url
            items['Img_link'] = book.xpath(".//div/a/img/@src").get()
            items['Price'] = new_price
            yield items


# class PilgrimsSpider(scrapy.Spider):
#     name = 'pilgrims'
#     book_name = "palpasa cafe"
#     allowed_domains = ['pilgrimsonlineshop.com']
#     start_urls = [f'https://www.pilgrimsonlineshop.com/search?q={book_name}']
#
#     def parse(self, response):
#         result_books = response.xpath(
#             "//div[@class='book-list']/ul/li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-2']/div[@class='zoom']")
#
#         for book in result_books:
#             price = book.xpath(".//div[@class='caption']/p/span/text()").get()
#             managed_price = price[4:]
#             new_price = float(managed_price) * 100
#             yield {
#                 'Book_Name': book.xpath(".//div[@class='caption']/h4/a/text()").get(),
#                 'Book_link': book.xpath(".//a/@href").get(),
#                 'Img_link': book.xpath(".//a/img/@src").get(),
#                 'Discounted_Price': new_price
#                 # 'No_discounted_Price': book.xpath(
#                 #     "normalize-space(.//a/div/div[@class='panel-footer']/small/text()[2])").get()
#             }

# from scrapy.crawler import CrawlerProcess
# process = CrawlerProcess()
# process.crawl(BooksmandalaSpider)
#
# process.start()