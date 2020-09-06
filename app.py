'''
downloadXkcd.py - Downloads every single XKCD comic.
'''

import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok= True)
limit = 10

while not url.endswith('#'):
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic= soup.select('#comic img')
    if comic == []:
        print('Could not find comic image.')
    else:
        comicUrl = f"https:{comic[0].get('src')}"
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prevLink.get('href')}"

    if limit<=0:
        break
    else:
        limit -= 1

print('Done')