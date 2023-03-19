import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['title', 'author', 'content'])

r = requests.get('https://poetrydb.org/author/all')

data = json.loads(r.text)

for d in data:
    df.loc[len(df)] = [d.get('title'), d.get('author'), '\n'.join(d.get('lines'))]

df.to_pickle('more_poems.pickle')