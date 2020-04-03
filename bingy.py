import webbrowser
import random_word
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

# r = random_word.RandomWords()
# search_items = r.get_random_words(limit=30)
# webbrowser.open_new("https://account.microsoft.com/rewards/pointsbreakdown")
# for item in search_items:
#     webbrowser.open("https://www.bing.com/search?q=" + item)

def start_bing_query(driver):
    rando = random_word.RandomWords()
    # buggy right now
    item = ""
    while True:
        try:
            item = rando.get_random_word()
            break
        except:
            print("rando did not work...trying again")

    while True:
        try:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://www.bing.com/search?q=" + item)
            
            break
        except NoSuchWindowException:
            print("No Such Window Exception: trying again")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # webbrowser.open("https://www.bing.com/search?q=" + item)

    

def list_of_words(size=10):
    rando = random_word.RandomWords()
    words = []
    attempts = 0
    while len(words < size) or attempts > 200:
        try:
            words.append(rando.get_random_word())
        except:
            print("random_words didn't work...trying again")
        attempts += 1
    
    return rando.get_random_words()
