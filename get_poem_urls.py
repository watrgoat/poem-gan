import requests
import json
from multiprocessing import Pool


def write(urls: set):
    # read past urls into set
    prev_urls = set()
    with open('urls.txt', mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            prev_urls.add(line.strip())
    
    print(f'# of old urls: {len(prev_urls)}')
    
    # get urls not already in file
    out_urls = urls.difference(prev_urls)
    print(len(out_urls))
    # append urls out to file
    with open('urls.txt', mode='a', encoding='utf-8') as f:
        for url in out_urls:
            f.write(url+'\n')
    return

hdrs = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15', 'Referer':'http://www.google.com/', 'Accept-Language':'en-gb'}

def main(num):
    r = requests.get(f"https://www.poetryfoundation.org/ajax/poems?page={num}&sort_by=recently_added", headers=hdrs)

    if r.status_code != 200:
        print("response not given")
        return

    data = json.loads(r.text)
    # possibly get snippet data for input, title, author?, tags, type
    urls = set()
    for d in data['Entries']:
        urls.add(d.get('link'))

    write(urls)
    print(f'Done on url #: {num}')
    return

if __name__ == '__main__':
    numbas = list(range(1, 5)) # change to what is being searched
    with Pool(3) as p:
        p.map(main, numbas)