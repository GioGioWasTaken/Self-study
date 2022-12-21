#making a typing bot for tenfastfingers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('https://10fastfingers.com/typing-test/english')
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'CybotCookiebotDialog')))
dontwantcookies=driver.find_element(By.ID,'CybotCookiebotDialogBodyButtonDecline')
dontwantcookies.click()
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,'highlight')))
word=driver.find_element(By.CLASS_NAME,'highlight').text
input=driver.find_element(By.ID,'inputfield')
for i in range(200):
    try:
        input.send_keys(word)
        input.send_keys(Keys.SPACE)
        word = driver.find_element( By.CLASS_NAME, 'highlight' ).text
        time.sleep(0.1)
    except:
        print('Finished')
#WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,'auswertung-result')))
time.sleep(100) #could potentially scrape the time elemenet and put it as amount of seconds.
#screenshot=driver.find_element(By.ID,'auswertung-result').find_element(By.ID,'a').get_attribute('href')
#print(screenshot)

