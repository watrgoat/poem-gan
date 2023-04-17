from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from multiprocessing import cpu_count
from multiprocessing import Pool
from pathlib import Path
import json


url_path = Path(r'scraping\urls.txt')
poem_path = Path(r'dataset\poems.pickle')

hdrs = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15', 'Referer':'http://www.google.com/', 'Accept-Language':'en-gb'}


def scrape_poetry_foundation(url):
    if url == '':
        return
    # need to check if poem is an image
    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code != 200:
        return
    
    soup = BeautifulSoup(r.text, features='html.parser')

    # get the poem text
    poem = str()
    for div in soup.find_all('div', {'style':'text-indent: -1em; padding-left: 1em;'}):
        line = div.text.replace('\xa0', '')
        line = re.sub("\s\s+" , " ", line)
        # remove extra spacing
        poem += line.strip()+'\n'
    poem = poem.strip()

    # get the poem tags
    ugly_tags = soup.find_all('a', href=re.compile('https://www.poetryfoundation.org/poems/browse#topics=[0-9]+'))
    tags = []
    for U_tag in ugly_tags:
        tags.append(U_tag.text)
    
    # get the poem title
    try:
        title = soup.find('h3', {'class': 'c-hdgSans c-hdgSans_5 c-mix-hdgSans_blocked'}).text
    except:
        title = ''
        
    try:
        author = soup.find('span', {'class':'c-txt c-txt_attribution'}).text.strip()[3:]
    except:
        author = ''

    return title, author, poem, tags


def get_poets_org(num) -> pd.DataFrame:
    print(f'working on: {num}')
    # gets 20 poems

    url = f'https://api.poets.org/api/poems?page={num}'

    r = requests.get(url, headers=hdrs)

    if r.status_code != 200:
        print("response not given")
        return

    df = pd.DataFrame(columns=['title', 'author', 'content', 'tags'])

    data = json.loads(r.text)
    
    for row in data.get('rows'):
        title = row['title']
        most_auth = row['field_author'].split('">')[-1]
        author = most_auth[:-4]
        tags = []
        clean = re.compile('<.*?>')
        poem = re.sub(clean, " ", row['body'])
        poem = re.sub("\s\s+" , "\n", poem)
        # remove extra spacing
        poem = poem.strip()
        df.loc[len(df)] = [title, author, poem, tags]

    return df


def get_urls():
    data_folder = Path("scraping/")
    file_path = data_folder / "urls.txt"
    with open(file_path, mode='r', encoding='utf-8') as f:
        urls = f.read()

    urls = urls.split('\n')
    
    return urls
    

def main():
    mass_df = pd.DataFrame(columns=['title', 'author', 'content', 'tags'])

    for i in range(1):
        mass_df = pd.concat([mass_df, get_poets_org(i)]) # max = 693
        mass_df.reset_index(drop=True, inplace=True)

    mass_df.to_pickle('poets_org.pickle')

if __name__ == '__main__':
    main()