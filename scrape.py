import requests
import random
from collections import Counter

def get_raw_text(url='test'):
    proxies = ['http://159.203.3.234', 'http://164.132.170.100', 'http://146.59.2.185', 'http://137.74.65.101', ] 
    proxy = {'http': random.choice(proxies)} 
    headers_list = [{ 
        'authority': 'httpbin.org', 
        'cache-control': 'max-age=0', 
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 
        'sec-ch-ua-mobile': '?0', 
        'upgrade-insecure-requests': '1', 
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
        'sec-fetch-site': 'none', 
        'sec-fetch-mode': 'navigate', 
        'sec-fetch-user': '?1', 
        'sec-fetch-dest': 'document', 
        'accept-language': 'en-US,en;q=0.9', 
    }] 
    headers = random.choice(headers_list) 
    return requests.get(url, headers=headers, proxies=proxy).text

def get_wordcount(text="SHOULD BE 3"):
    split_text = text.split()
    bl = [';', '-', '.', '_', '<', '>', '=', '%', '@', '{', '}', '[', ']', '(', ')', '\\', '/', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
    for c in bl:
        split_text = [ x for x in split_text if c not in x ]
    print(split_text)
    return len(split_text) * 0.95

def get_common_words(text='TESTING THIS SCRIPT'):
    split_text = text.lower().split()
    bl = ['<', '>', '=', '%', '@', '}', '{', '[', ']', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'in', 'and', 'with', 'can', 'be', 'made', 'you', 'of', 'the', 'from', 'for']
    for c in bl:
        split_text = [ x for x in split_text if c not in x ]
    split_text = [x for x in split_text if len(x) >= 3]
    
    found = Counter(split_text)
    return found.most_common(5)

def get_percent_words(text=' '):
    wordcount = get_wordcount(text=text)
    common_words = get_common_words(text=text)
    words_percent = {}

    for word in range(len(common_words)):
        words_percent[common_words[word][0]] = (float(common_words[word][1]) / wordcount) * 100

    return words_percent
