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

global driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)


def scrape_urls(url):
    print(url)
    num_links = 20

    driver.get(f"https://www.poetryfoundation.org/poems/browse#page={url}&sort_by=recently_added") # load the page

    # give it some time
    driver.implicitly_wait(45)
    time.sleep(2)

    html_source = driver.page_source

    soup = bs.BeautifulSoup(html_source, features="html.parser")

    out_urls = set()

    for aHref in soup.find_all("a",href=re.compile('.*/poems/[0-9]+/.*')):
        out_urls.add(aHref.get("href"))
    
    return out_urls


def gen_urls(num):
    urls = []
    for i in range(num):
        urls.append(f"https://www.poetryfoundation.org/poems/browse#page={i+1}&sort_by=recently_added")
    
    return urls


def main():
    start = time.time()
    num_urls = 1000 # number of urls wanted to be generated: max is 2341
    num_processes = cpu_count() # returns the number of vcpus available
    chunksz = int(num_urls//num_processes)

    out_urls = set()
    with Pool(num_processes) as p:
        for result in p.map(scrape_urls, range(1, num_urls+1), chunksize=chunksz):
            out_urls |= result
    
    with open('urls.txt', 'w') as f:
        for url in out_urls:
            f.write(url+'\n')
    
    end = time.time()
    print(f"Time spent: {end-start}")
    # 3 sec time: 108
    # 3 sec count: 776 ?????
    # 2 sec 10b time: 83
    # 2 sec 10b count: 931
    # 2 sec time: 77
    # 2 sec count: 792
    # 1 sec time: 48
    # 1 sec count: 596

if __name__ == "__main__":
    main()
