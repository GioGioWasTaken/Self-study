import scrapy
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ..items import AnilistTopItem
import time
class anilist_spider(scrapy.Spider):
    name='Anilist'
    start_urls = ['https://anilist.co/search/anime/top-100']
    def __init__(self):
        myoptions=ChromeOptions()
        myoptions.headless=True
        myoptions.add_experimental_option( "excludeSwitches", ["enable-automation"] )
        myoptions.add_experimental_option( 'useAutomationExtension', False )
        myoptions.add_argument( '--disable-blink-features=AutomationControlled' )
        myoptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36" )
        self.driver=webdriver.Chrome(options=myoptions)
        self.driver.get('https://anilist.co/search/anime/top-100')
        #self.parse(response=self.driver.page_source)
    def parse(self, response, **kwargs):
        items=AnilistTopItem()
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #Could possibly create a script that scrolls down until it detects a #rank value that's bigger than x.
        self.driver.implicitly_wait( 10 )
        res=response.replace(body=self.driver.page_source)
        anime_boxes=res.css('div.media-card')
        for anime_box in anime_boxes:
            title=anime_box.css('a.title::text').get().replace('\n','').replace('\t','')
            score=anime_box.css('span.percentage::text').get().replace('%','') #convert from % to decimal.
            score=str(int(score)/10) #same as the former comment.
            rank=anime_box.css('div.rank.circle::text').get().replace('\n','').replace('\t','')
            date = anime_box.css('div.date::text').get()
            items['title']=title
            items['score']=score
            items['rank'] = rank
            items['date'] = date
            yield items
