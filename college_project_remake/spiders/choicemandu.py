# -*- coding: utf-8 -*-
import scrapy

from college_project_remake.items import CollegeProjectRemakeItem
from college_project_remake.Controller import book_name

class ChoicemanduSpider(scrapy.Spider):
    name = 'choicemandu'
    allowed_domains = ['choicemandu.com']
    start_urls = [
        f'https://choicemandu.com/index.php?category_id=0&search={book_name}&submit_search=&route=product%2Fsearch']

    def parse(self, response):
        items = CollegeProjectRemakeItem()
        result_books = response.xpath("//div[@class = 'product-item-container']")

        for book in result_books:
            price = book.xpath(".//div[@class='right-block']/div[@class='price']/span/text()").get()
            managed_price = price[3:]
            new_price = float(managed_price)
            new_price = int(new_price)

            items['Name'] = book.xpath(".//div/h2[@class='product-name-edited']/a/text()").get()
            items['Book_link'] = book.xpath(".//div/div/a/@href").get()
            items['Img_link'] = book.xpath(".//div/div/a/img/@data-src").get()
            items['Price'] = str(new_price)
            yield items
            # 'No_discounted_Price': book.x
            #     "normalize-space(.//a/div/div[@class='panel-footer']/small/text()[2])").get()

