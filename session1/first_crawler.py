import requests
from bs4 import BeautifulSoup

resp = requests.get('https://behappycc.github.io/web_scraping_with_python/session1/first_crawler.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)