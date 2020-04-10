import requests
import random

class Rando:
    def __init__(self):
        all_words = requests.get("http://svnweb.freebsd.org/csrg/share/dict/words?view=co", stream=True)
        self.words = [word.decode('utf-8') for word in all_words.iter_lines()]
        self.length = len(self.words)
    
    def get_random_word(self):
        rand_num = random.randint(0, self.length-1)
        return self.words[rand_num]

# r = Rando()
# print(r.get_random_word())