import webbrowser
import random_word

# r = random_word.RandomWords()
# search_items = r.get_random_words(limit=30)
# webbrowser.open_new("https://account.microsoft.com/rewards/pointsbreakdown")
# for item in search_items:
#     webbrowser.open("https://www.bing.com/search?q=" + item)

def start_bing_query():
    rando = random_word.RandomWords()
    item = rando.get_random_word()
    webbrowser.open("https://www.bing.com/search?q=" + item)