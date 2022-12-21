import scrapy
from ..items import MalTopItem
class MAL_spider(scrapy.Spider):
    name='MAL'
    start_urls=['https://myanimelist.net/topanime.php']
    def parse(self, response, **kwargs):
        items = MalTopItem()
        anime_boxes=response.css('tr.ranking-list')
        for anime_box in anime_boxes:
            title = anime_box.css('h3.hoverinfo_trigger.fl-l.fs14.fw-b.anime_ranking_h3 a::text').extract()
            score = anime_box.css( 'span.text.on.score-label::text').extract()
            rank=anime_box.css('span.lightLink.top-anime-rank-text::text').extract()
            items['title']=title
            items['score'] = score
            items['rank'] = rank
            yield items
        next_50 = response.css('a.link-blue-box.next::attr("href")').get()
        if next_50!='?limit=400': #set the limit, if you want all of them, do: if not None
            next_50='https://myanimelist.net/topanime.php' + next_50 #set the link
            yield response.follow(next_50, callback=self.parse,dont_filter=True) #parse the page now that it pressed the next_50 btn