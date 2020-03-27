import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):

    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    if len(comicElem) is 0:
        print('Unable to find comic images.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print(f'Downloading image {comicUrl}')
        comic = requests.get(comicUrl)
        comic.raise_for_status()
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), "wb") as imgF:
            for chunk in comic.iter_content(100000):
                imgF.write(chunk)
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

    # Optionally break after 6 images
    if(len(os.listdir('xkcd'))) == 6:
        break

print('Done.')