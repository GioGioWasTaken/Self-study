#THIS FILE WAS USED TO TEST AND DEBUG THE ERRORS I WAS GETTING IN 'Anilist_top'.
# **ISSUE RESOLVED **
#**THE CAUSE WAS THE HEADLESS PROPRETY. THE FIX WAS IMPLEMENTING THE OPTIONS SEEN BELOW**


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
options = ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

driver=webdriver.Chrome()

url=driver.get('https://anilist.co/search/anime/top-100')
driver.implicitly_wait(10)
#sourcecode=driver.find_elements(By.ID,'app')
#print(sourcecode.text)
time.sleep(4)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(driver.page_source)
anime_boxes=driver.find_elements(By.CSS_SELECTOR,'div.media-card')

#for anime_box in anime_boxes:
#    title=anime_box.find_element(By.CSS_SELECTOR,'a.title').text
#    score=anime_box.find_element(By.CSS_SELECTOR,'span.percentage').get_attribute("innerHTML")
#    date=anime_box.find_element(By.CSS_SELECTOR,'div.date').get_attribute("innerHTML")
#    print(f'title: {title}\nScore: {score}\nDate: {date}')
