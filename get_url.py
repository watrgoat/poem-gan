import bs4 as bs
import re

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
# pass the defined options and service objects to initialize the web driver


def scrape_urls(pg_num: int):
    driver = Chrome(options=options, service=chrome_service)
    driver.implicitly_wait(5)

    link = f"https://www.poetryfoundation.org/poems/browse#page={pg_num}&sort_by=recently_added"

    driver.get(link) # load the page

    # give it some time
    driver.implicitly_wait(45)
    time.sleep(5)

    html_source = driver.page_source

    soup = bs.BeautifulSoup(html_source, features="html.parser")

    out_urls = set()

    for aHref in soup.find_all("a",href=re.compile('.*/poems/[0-9]+/.*')):
        out_urls.add(aHref.get("href"))
    
    return out_urls


def write(urls: set):
    # read past urls into set
    with open('urls.txt', mode='r', encoding='utf-8') as f:
        prev_urls = set(f.readlines()[0].split(' '))
    
    print(f'# of urls: {len(prev_urls.union(urls))}')

    # get urls not already in file
    out_urls = urls.difference(prev_urls)

    # append urls out to file
    with open('urls.txt', mode='a', encoding='utf-8') as f:
        for url in out_urls:
            f.write(url+' ')
    return


def main():
    start = time.time()
    num_urls = 200 # number of urls wanted to be generated: max is 2341
    num_processes = cpu_count() # returns the number of vcpus available

    out_urls = set()
    with Pool(num_processes) as p:
        for result in p.map(scrape_urls, range(100, num_urls+1), chunksize=10):
            out_urls |= result
    
    write(out_urls)
    
    end = time.time()
    print(f"Time spent: {end-start}")


if __name__ == "__main__":
    main()
