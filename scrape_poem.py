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

hdrs = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15', 'Referer':'http://www.google.com/', 'Accept-Language':'en-gb'}

def scrape_poem(url):
    # need to check if poem is an image
    r = requests.get(url, headers=hdrs, allow_redirects=False)
    if r.status_code != 200:
        return
    
    soup = BeautifulSoup(r.text, features='html.parser')

    # get the poem text
    poem = ''
    for div in soup.find_all('div', {'style':'text-indent: -1em; padding-left: 1em;'}):
        poem += div.text.strip()+'\n'

    # get the poem tags
    ugly_tags = soup.find_all('a', href=re.compile('https://www.poetryfoundation.org/poems/browse#topics=[0-9]+'))
    tags = []
    for U_tag in ugly_tags:
        tags.append(U_tag.text)
    
    # get the poem title
    title = soup.find('h3', {'class': 'c-hdgSans c-hdgSans_5 c-mix-hdgSans_blocked'}).text

    author = soup.find('span', {'class':'c-txt c-txt_attribution'}).text.strip()[3:]

    return title, author, poem.strip(), tags


def get_urls():
    with open('urls.txt', mode='r', encoding='utf-8') as f:
        urls = f.read()

    urls = urls.split('\n')
    
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
    urls = urls[:10]
    print(len(urls))
    # with Pool(cpu_count()) as p:
    #     results = p.map(scrape_poem, urls)
    for url in urls:
        print(scrape_poem(url))


if __name__ == '__main__':
    main()