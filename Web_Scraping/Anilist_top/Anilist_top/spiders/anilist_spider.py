import scrapy
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
class anilist_spider(scrapy.Spider):
    name='Anilist'
    start_urls = ['https://anilist.co/search/anime/top-100']
    #myoptions=ChromeOptions()
    #myoptions.headless=True
    #driver=webdriver.Chrome(options=myoptions)
    #driver.get('https://anilist.co/search/anime/top-100')
    #selenium_response_text=driver.page_source
    def parse(self, response, **kwargs):
        anime_boxes=response.css('div.media-card')
        for anime_box in anime_boxes:
            title=anime_box.css('a.title::text').get().replace('\n','')
            #score=anime_box.css('div.score').get().replace('%','') #converting % to decimal
            #score=int(score)/10
            yield{'title':title}
            date = anime_box.css( 'div.date' )