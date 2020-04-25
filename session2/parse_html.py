import requests
from bs4 import BeautifulSoup

response = requests.get("https://behappycc.github.io/web_scraping_with_python/session2/parse_html.html")
print(response.text)
soup = BeautifulSoup(response.text, "html5lib") # 印出 h1 標籤

h1_text = soup.find("h1")
print(f'h1: {h1_text}')
print(f'h1: {h1_text.text}')
print(f'find_all p: {soup.find_all("p")}')
print(f'p: {soup.find("p").text}')
print(f'class blue: {soup.find("", {"class":"blue"})}')
print(f'id green: {soup.find("div", id="green").text}')
print(f'a href: {soup.find("a")["href"]}')
