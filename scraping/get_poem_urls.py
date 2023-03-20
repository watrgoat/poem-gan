import requests
import json
from multiprocessing import Pool
from pathlib import Path
from multiprocessing import cpu_count


url_path = Path(u'scraping\urls.txt')

# read past urls into set
with open(url_path, mode='r', encoding='utf-8') as f:
    urls = f.read()
    prev_urls = set(urls.split('\n'))


# write urls back into txt file
def write(urls: set):
    global prev_urls

    print(f'# of old urls: {len(prev_urls)}')
    
    # get urls not already in file
    out_urls = urls.difference(prev_urls)
    print(len(out_urls))
    # append urls out to file
    with open(url_path, mode='a', encoding='utf-8') as f:
        for url in out_urls:
            f.write(url+'\n')
    
    prev_urls |= out_urls
    return


hdrs = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15', 'Referer':'http://www.google.com/', 'Accept-Language':'en-gb'}


def get_urls(num):
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


def main():
    numbas = list(range(1, 5))
    processes = int(cpu_count()*.75)
    
    with Pool(3) as p:
        p.map(get_urls, numbas)


if __name__ == '__main__':
    main()