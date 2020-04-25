import requests
from bs4 import BeautifulSoup


def main():
    url1 = 'https://behappycc.github.io/web_scraping_with_python/first_crawler.html'
    bad_url = 'http://non-existed.domain/first_crawler.html'
    text1 = get_tag_text(url1, 'h1')
    print(text1)
    text2 = get_tag_text(url1, 'h2')
    print(text2)
    text3 = get_tag_text(bad_url, 'h1')
    print(text3)


def get_tag_text(url, tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(tag).text
    except Exception as e:
        print('Exception: %s' %(e))
    return None


if __name__ == '__main__':
    main()