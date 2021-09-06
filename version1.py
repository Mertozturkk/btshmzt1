import requests
from bs4 import BeautifulSoup as bs
import hashlib
import pandas as pd
import numpy as np

site = "http://www.sahibinden.com/kategori-vitrin?viewType=List&category=3530"
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
# Sitenin negelleyebileceği bot vb. durumlar ve hata almamak için header oluşturduk
ITEM_URL_ = []
ITEM_URL_SHA1 = []

URL_SHA1 = hashlib.sha1(site.encode())


def scraper():
    r = requests.get(site,headers = headers)   #İlgili sayfadan request isteğimizi alıyoruz
    soup = bs(r.content,'html.parser')
    links = soup.find("tbody", class_="searchResultsRowList") # linklere ulaşabilmek için tbody ve ilgili classa ulaştık
    
    for a in links.find_all('a', href=True): #linkleri bir listeye topladık
        ITEM_URL_.append(a['href'])
    if "#" in ITEM_URL_:                     # linkler arasında listeye eklenen '#' işaratlerini eğer varsa genel listemizden sildik
        hasht_=ITEM_URL_.count('#')
        for _ in range(hasht_):
            ITEM_URL_.remove('#')

    
    for link in ITEM_URL_:                      # eklenen her bir link için SHA1 oluşturuldu
        SHA1_ITEM =hashlib.sha1(link.encode())
        ITEM_URL_SHA1.append(SHA1_ITEM.hexdigest())

    ITEM_URL = pd.DataFrame(ITEM_URL_)
    ITEM_URL.to_csv('ITEM_URL.csv')

    ITEM_URL_SHA2 = pd.DataFrame(ITEM_URL_SHA1)
    ITEM_URL_SHA2.to_csv('ITEM_URL_SHA1.csv')






if __name__== "__main__":
    scraper()

