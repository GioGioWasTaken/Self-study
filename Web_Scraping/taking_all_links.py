from bs4 import BeautifulSoup
import requests
wikipedia_page=requests.get('https://en.wikipedia.org/wiki/Easter_Island')
soup=BeautifulSoup(wikipedia_page.text,'lxml')
session = requests.Session()
wiki_body=soup.find('div','vector-body')
wiki_links=wiki_body.find_all('p')
namelist=[]
linklist=[]
for wiki_link in wiki_links:
    a_tags=wiki_link.find_all('a')
    for a_tag in a_tags:
        print(a_tag.parent())
        if a_tag.parent(): #no idea how to compare tags and text comparisions don't seem to work
            article_name=a_tag.text
            namelist.append(article_name)
            article_link=a_tag.get('href')
            linklist.append(article_link)
        else:
            print(a_tag.parent())
print(namelist)
print(linklist)
#    linklist.append(shorturl.url)
#    print('Was not a link')
#    article_name=wiki_link.text
#    namelist.append(article_name)
#print(namelist)
#print(f"These are supposed to be links: {linklist} ")