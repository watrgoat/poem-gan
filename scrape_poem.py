from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

# For simulating the table on the webpage which is dynamically loaded.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome 

from multiprocessing import cpu_count
from multiprocessing import Pool
import time

global options
global chrome_service

chrome_path = ChromeDriverManager().install() #Path for my Chrome driver.
options = webdriver.ChromeOptions()
options.add_argument('--headless') # it's more scalable to work in headless mode 
# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none'
# this returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)

def scrape_poem(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, features='html.parser')
    result = soup.find_all('div', {'style':'text-indent: -1em; padding-left: 1em;'})

    for div in result:
        print(div.text.strip())
    return


def get_urls():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()[0].split(' ')
    
    return urls

def main():
    urls = get_urls()
    print(len(urls))

    scrape_poem('https://www.poetryfoundation.org/poetrymagazine/poems/159609/11-violence-anglo-linguistic')


if __name__ == '__main__':
    main()