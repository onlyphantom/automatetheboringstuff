import requests, sys, webbrowser, bs4
from fake_useragent import UserAgent

ua = UserAgent()
res = requests.get('https://duckduckgo.com/?q=' + ' '.join(sys.argv[1:]), {"User-Agent": ua.random})
# res.raise_for_status()
with open('downloaded.html', 'wb') as f:
    for chunk in res.iter_content(10000):
        f.write(chunk)

soup = bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.find_all('result__url', limit=5)

for i in range(len(linkElems)):
    if i == 1:
        webbrowser.open('linkElems[i].get("href")')
    else:
        webbrowser.open_new_tab('linkElems[i].get("href")')
