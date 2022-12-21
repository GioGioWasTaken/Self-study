# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3
class LearningScrapyPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect("quotes.db")
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""") #the program will be run more than once, so we must drop the table and put a new one in it's place.
        self.curr.execute("""CREATE TABLE quotes_tb(The_quote TEXT,Author TEXT,Tag TEXT)""") #creating the table
    def process_item(self, item,spider):
        self.store_db(item)
    def store_db(self,item):
        self.curr.execute("""INSERT INTO quotes_tb VALUES(?,?,?)""",(
            item['quote_text'][0],
            item['author'][0],
            item['tag'][0]))
        self.conn.commit()