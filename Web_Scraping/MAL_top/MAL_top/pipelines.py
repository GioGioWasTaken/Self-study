# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class MalTopPipeline():

    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect("MAL.db")
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS MAL_tb""") #the program will be run more than once, so we must drop the table and put a new one in it's place.
        self.curr.execute("""CREATE TABLE MAL_tb(Title TEXT,Score TEXT,Rank TEXT)""") #creating the table
    def process_item(self, item, spider):
        self.store_db(item) #call the store_db function
    def store_db(self,item):
        self.curr.execute("""INSERT INTO MAL_tb VALUES(?,?,?)""",(
            item['title'][0],
            item['score'][0],
            item['rank'][0]))
        self.conn.commit()