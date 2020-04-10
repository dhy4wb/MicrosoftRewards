import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
from bingy import start_bing_query
import rando_word_gen
#from bingy import list_of_words
'''
    Selenium is necessary because of the javascript that is 
    loaded.
    The ordinary Python request will not render the html after
    a certain bit.
'''
link = "https://account.microsoft.com/rewards/pointsbreakdown"
driver = webdriver.Edge()
#sometimes will fail, maybe put a try statement to retry until fixed
while True:
    try:
        driver.get(link)
        break
    except NoSuchWindowException:
        print("No Such Window Exception: trying again")
    


driver.implicitly_wait(10)
userPointsBreakdown = WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("userPointsBreakdown"))
# print(userPointsBreakdown.text)
# print(userPointsBreakdown.tag_name)
soup = BeautifulSoup(driver.page_source, 'html.parser')
all = soup.find_all('p', class_="pointsDetail c-subheading-3 ng-binding")
numbers = all[0].get_text().split(' / ')
numbers = list(map(int, numbers))
print(numbers)
r = rando_word_gen.Rando()
while numbers[0]/numbers[1] < 1:
    start_bing_query(driver, r)
    driver.refresh()
    time.sleep(5)
    WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("userPointsBreakdown"))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    all = soup.find_all('p', class_="pointsDetail c-subheading-3 ng-binding")
    numbers = all[0].get_text().split(' / ')
    numbers = list(map(int, numbers))
    print(numbers)

time.sleep(10)
driver.quit()
# print(all)
# all_div = soup.find_all(True)
# print(len(all_div))
# for tag in all_div:
#     print(tag.name)
