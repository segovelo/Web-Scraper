# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:06:51 2021

@author: Sebastian
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

productlinks = []
for x in range(1,6):
    k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text  
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})
    #print(productlist)
    
    
    for product in productlist:
            link = product.find("a",{"class":"product-card"}).get('href')  
            productlinks.append(baseurl + link)

print(len(productlinks))