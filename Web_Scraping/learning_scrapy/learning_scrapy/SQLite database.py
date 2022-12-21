import sqlite3
from spiders import First_spider
conn = sqlite3.connect('quotes.db') #establish a connection between sqlite and the database created
curr=conn.cursor()

curr.execute("""CREATE TABLE IF NOT EXISTS quotes_tb(quote_text TEXT,author TEXT,tag TEXT)""")
curr.execute("""INSERT INTO quotes_tb
VALUES('Python is cool' , 'me' , 'python')""")

conn.commit()
conn.close()