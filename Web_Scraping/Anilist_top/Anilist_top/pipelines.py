# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AnilistTopPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect('Anilist_top.db')
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS Anilist_tb""" )  # the program will be run more than once, so we must drop the table and put a new one in it's place.
        self.curr.execute( """CREATE TABLE Anilist_tb(Title TEXT,Score TEXT,Rank TEXT,Date TEXT)""" )  # creating the table
    def process_item(self, item, spider):
        self.store_db(item) #adds it to the data base
        return item #prints the item on the terminal
    def store_db(self,item):
        self.curr.execute("""INSERT INTO Anilist_tb VALUES(?,?,?,?)""",(
            item['title'],
            item['score'],
            item['rank'],
            item['date']))
        self.conn.commit()