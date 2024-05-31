#Author: Lorenzo Castellini Coutin

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd
import csv

driver = webdriver.Chrome()

URL = 'https://www.newegg.com/p/pl?d=rtx+4070'

driver.get(URL)

soup = BeautifulSoup(driver.page_source, 'html.parser')

GPUs = soup.find_all('a', {'class' : 'item-title'})

for g in GPUs:
    print(g.get_text())

prices = soup.find_all('li', {'class' : 'price-current'})

for p in prices:
    price_tag = p.find('strong')

    if price_tag:
        print("$" + str(price_tag.get_text()))

links = soup.find_all('a', {'class' : 'item-title'})

for l in links:
    full_links = l.get('href')
    print(full_links)










 





