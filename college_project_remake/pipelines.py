import mysql.connector
class MysqlPipeline(object):
    def __init__(self):
        self.create_connection()
        #self.create_table()
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "9849559082",
            database ="books_db"
        )
        self.mydb =self.conn.cursor()
    # def create_table(self):
    #    # self.mydb.execute(""" DROP TABLE IF EXISTS palpasa_cafe""")
    #     self.mydb.execute("""create table palpasa_cafe(
    #         Name text,
    #         Book_link text,
    #         Img_link text,
    #         Price text
    #     )
    #     """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.mydb.execute("""insert into Books values(%s,%s,%s,%s)""",
                          (
                              item['Name'],
                              item['Book_link'],
                              item['Img_link'],
                              item['Price']
                          )
                          )
        self.conn.commit()
