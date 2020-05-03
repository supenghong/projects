# Gets URLs from YouTube Watch Later playlist
import logging, pyperclip, requests, bs4, pprint
from selenium import webdriver

logging.basicConfig(level=logging.INFO,
                    format='%(message)s')
logging.disable(logging.CRITICAL)

url = ("https://www.youtube.com/"
       "playlist?list=PLVXrLc-IGQj_S0TBY7Lwlt02odTuvr0kC")

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Find link elements
links = []
linkElems = soup.select('#content a')

for elem in linkElems:
    if elem.get('href').startswith("/watch?v="):
        # Split href element by & and take only the actual video link
        linkUrl = "https://www.youtube.com" + elem.get('href').split('&')[0]
        if linkUrl not in links:
            links.append(linkUrl)

# Copy to clipboard
allLinks = '\n'.join(links)
pyperclip.copy(allLinks)
