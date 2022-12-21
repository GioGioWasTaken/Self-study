# What should the update do?
# Steam sales bot 4.0 should scarpe all the data without sorting through it, and then make a file.
# There should than be a new program that reads the txt file, and makes a new sub-txt file, that has user-defined critiria based info in it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wanted_percentage = int(input('Please enter the minimum discount percentage you are willing to buy games for:'))

driver = webdriver.Chrome()  # set up webdriver, bs cannot scarpe dynmic(?) pages by itself.
url_selenium = driver.get('https://store.steampowered.com/specials')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to the bottom so it loads everything, please attempt to make it scroll to "show more" in future versions
print(url_selenium)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))  # wait so it loads everything
html_loaded = driver.page_source  # only than take the page sourceg = 0  # will be used to determine the offset of the steam page
g=  0
o = 396  # will be used to have something(that i can change at a given time) to match g with

def take_stats():
    global sales
    WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))
    sales = driver.find_elements(By.CLASS_NAME,'salepreviewwidgets_SaleItemBrowserRow_y9MSd')
    for sale in sales:
        game_link = sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleWidgetHalfLeft_2Va3O').find_element(By.TAG_NAME,'a').get_attribute('href')
        try:
            WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,'salepreviewwidgets_StoreSaleDiscountBox_2fpFv')))
            sale_percentage=sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleDiscountBox_2fpFv').text
        except:
            print('No sale for this game')
            continue
        game_name=sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreSaleWidgetTitle_3jI46').text
        game_price = sale.find_element(By.CLASS_NAME,'salepreviewwidgets_StoreOriginalPrice_1EKGZ').text
        game_price_discounted = sale.find_element(By.CLASS_NAME, 'salepreviewwidgets_StoreSalePriceBox_Wh0L8').text
        byepercents = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  # get rid of % and - so i can compare the percent of sale_percent with the user set wanted_percentage variable.
        newlist = []
        i = 0
        for letter in sale_percentage:
            if sale_percentage[i] in byepercents:
                newlist.append(letter)
            i = i + 1
        sale_percentage = int(newlist[0] + newlist[1])
        if sale_percentage >= wanted_percentage:
            print(f' ⌜———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————⌝\n│"{game_name}" is {sale_percentage}% off. The original price is {game_price} and the current price is {game_price_discounted}│ \n│The game on Steam: {game_link}.│\n ⌞_______________________________________________________________________________________________________________________⌟\n')
def show_more1():
    global g, sales
    show_more = driver.find_element(By.CLASS_NAME, 'saleitembrowser_ShowContentsContainer_3IRkb').find_element(By.TAG_NAME, 'button')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'saleitembrowser_ShowContentsContainer_3IRkb')))
    show_more.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    g = g + 13
    WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'salepreviewwidgets_SaleItemBrowserRow_y9MSd')))
    print(f'The approximated offset is:{g}')
    return g


def show_more_all():
    global o, html_loaded, url_selenium
    while g < o-13:
        driver.implicitly_wait(20)
        show_more1()
    else:
        take_stats()
        url_selenium = driver.get(f'https://store.steampowered.com/specials?offset={g}')  # an attempt to change the url to the g offset, after testing might change to {g-13}/{g+13} too tired to tell which as of now
        html_loaded = driver.page_source
        o = o + 396  # I want the process to be repeated 10 times.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


while g < 3968:
    show_more_all()