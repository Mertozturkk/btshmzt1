import requests
from bs4 import BeautifulSoup as bs
import hashlib

site = "http://www.sahibinden.com/kategori-vitrin?viewType=List&category=3530"
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
urls = []
def scraper():
    r = requests.get(site,headers = headers)
    soup = bs(r.content,'html.parser')
    tags = soup.find("tbody", class_="searchResultsRowList")
    
    for a in tags.find_all('a', href=True):
        urls.append(a['href'])
    if "#" in urls:
        hasht_=urls.count('#')
        for _ in range(hasht_):
            urls.remove('#')
    
    for link in urls:
        SHA1_ITEM =hashlib.sha1(link.encode())
        print(SHA1_ITEM.hexdigest())


URL_SHA1 = hashlib.sha1(site.encode())
print("Site SHA1 : ", URL_SHA1.hexdigest())




if __name__== "__main__":
    scraper()
