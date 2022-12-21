import scrapy

from ..items import LearningScrapyItem

class Quotespider(scrapy.Spider):
    name='quotes'
    start_urls=['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):

        items = LearningScrapyItem()
        all_quote_boxes=response.css('div.quote')
        for quote_box in all_quote_boxes:
            quote_text=quote_box.css('span.text::text').extract()
            author=quote_box.css('.author::text').extract()
            tag=quote_box.css('.tag::text').extract()
            #tag=' '.join(tag)
            items['quote_text']=quote_text
            items['author']= author
            items['tag'] = tag
            yield items
        next_btn = response.css('li.next a::attr(href)').get()
        if next_btn is not None:
            yield response.follow(next_btn,callback=self.parse)