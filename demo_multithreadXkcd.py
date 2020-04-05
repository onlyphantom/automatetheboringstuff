import os, threading
import requests, bs4

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        url = f'http://xkcd.com/{urlNumber}'
        print(f'Downloading:', url)
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
            with open(os.path.join('xkcd', os.path.basename(comicUrl)), "wb") as f:
                for chunk in comic.iter_content(100000):
                    f.write(chunk)
            
downloadThreads = []
# create 5 threads, each call downloadXkcd() 4 times
for i in range(1, 50, 10):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+4))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# calling .join() will block until that thread has finished
# .join is called by main-thread, to stop main-thead from executing until
# the execution of joined thread is complete.
for thread in downloadThreads:
    thread.join()
print('Done.')