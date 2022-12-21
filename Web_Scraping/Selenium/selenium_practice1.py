from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
url=driver.get('https://clickspeedtest.com')
completion_screen = driver.find_element( By.CLASS_NAME, 'modal-popup')


def auto_clicker():
 driver.implicitly_wait(30) #instead of time.sleep, in case the element is found before the specified time.
 my_element=driver.find_element(By.ID,'clicker')
 for i in range(100):
  my_element.click()
 WebDriverWait( driver, 10 ).until(
  EC.visibility_of_element_located((By.CLASS_NAME,'modal-popup')))
 time.sleep(2)
 driver.quit()
auto_clicker()