from bs4 import BeautifulSoup
import requests
import re

# For simulating the table on the webpage which is dynamically loaded.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome 

from multiprocessing import cpu_count
from multiprocessing import Pool
import time


def scrape_poem(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, features='html.parser')

    result = soup.find_all('div', {'style':'text-indent: -1em; padding-left: 1em;'})
    poem = ''
    for div in result:
        poem += div.text.strip()+'\n'

    ugly_tags = soup.find_all('a', href=re.compile('https://www.poetryfoundation.org/poems/browse#topics=[0-9]+'))
    tags = []

    for U_tag in ugly_tags:
        tags.append(U_tag.text)

    return tags


def get_urls():
    with open('urls.txt', 'r', encoding='utf-8') as f:
        urls = f.readlines()[0].split(' ')
    
    return urls


def save_data(data):
    # loop over elements
    # sub list[0] = poem title
    # sub list[1] = poet name
    # sub list[2] = poem content
    # sub list[3] = tags????

    pass


def main():
    urls = get_urls()
    test_url = 'https://www.poetryfoundation.org/poetrymagazine/poems/159609/11-violence-anglo-linguistic'
    print(len(urls))
    
    # with Pool(cpu_count()) as p:
    #     results = p.map(scrape_poem, urls)
    
    print(scrape_poem(test_url))


if __name__ == '__main__':
    main()