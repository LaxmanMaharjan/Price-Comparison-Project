import mysql.connector
from operator import itemgetter  # i imported it for sorting purpose

book_name = 'karnali blues'  # Enter the book name to scrape information about from all spider websites


class PriceComparator:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="9849559082",
            database="books_db"
        )
        self.cursor = self.conn.cursor()

    def Compare(self):
        self.cursor.execute(f"select distinct * from books where name like '%{book_name}%'")  # sorts in ascending order
        self.results = self.cursor.fetchall()  # this results is the list of tuple of info in order of name,book_link,img_link and price
        return self.results

    def get_individual(self):
        self.Names = []  # these are each lists of info in according to name of the list
        self.Book_links = []
        self.Img_links = []
        self.Price = []
        for result in self.results:
            self.Names.append(result[0])
            self.Book_links.append(result[1])
            self.Img_links.append(result[2])
            self.Price.append(result[3])
        collection = [self.Names, self.Book_links, self.Img_links, self.Price]
        return collection


ob = PriceComparator()
book_list = ob.Compare()
sorted_book_list = sorted(book_list, key=itemgetter(3))
print(book_list)
print(sorted_book_list)
