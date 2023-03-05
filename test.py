from requests_html import HTMLSession

session = HTMLSession()
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
links = []
url = f"https://www.poetryfoundation.org/poems/browse#page=1&sort_by=recently_added"
r = session.get(url, headers=headers)
r.html.render()
links += r.html.absolute_links

print(set(links))