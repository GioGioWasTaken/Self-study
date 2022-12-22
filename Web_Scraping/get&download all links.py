import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
def download_website(url):
    response = requests.get(url)
    return response.text
url=driver.get('https://gadial.net/post_list/?s=')
post_links=driver.find_elements(By.CSS_SELECTOR,'a.post-link[href]')
for post_link in post_links:
    new_post_link=post_link.get_attribute('href')
    print(new_post_link)
    download_website(new_post_link)