import requests
from bs4 import BeautifulSoup


def scrappingJapanRegionData():

    url = "http://www.welcometojapan.or.kr/location/regional/ishikawa/kagaonsenkyou.html"
    html = requests.get(url)
    soup = BeautifulSoup(html.content.decode('utf-8', 'replace'), 'html5lib')
    print(soup)

if __name__ == "__main__":

    scrappingJapanRegionData()
