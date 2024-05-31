#Author: Lorenzo Castellini Coutin

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd
import csv
import pyshorteners

file_path ='GPU_Data.csv'

GPU_list = []
prices_list = []
links_list = []

driver = webdriver.Chrome()

URL = 'https://www.newegg.com/p/pl?d=rtx+4070'

driver.get(URL)

soup = BeautifulSoup(driver.page_source, 'html.parser')

GPUs = soup.find_all('a', {'class' : 'item-title'})

for g in GPUs:
    GPU_list.append(g.get_text())

prices = soup.find_all('li', {'class' : 'price-current'})

for p in prices:
    price_tag = p.find('strong')

    if price_tag:
        prices_list.append("$" + str(price_tag.get_text()))

links = soup.find_all('a', {'class' : 'item-title'})

for l in links:
    full_links = l.get('href')
    shortener = pyshorteners.Shortener()
    short_links = shortener.tinyurl.short(full_links)
    links_list.append(short_links)


with open(file_path, 'w', newline = '') as csv_file:
    GPU_data = csv.writer(csv_file)
    GPU_data.writerow(['Item', 'Price', 'Shop Links (Newegg.com)'])
    
    for g, p, l in zip(GPU_list, prices_list, links_list):
        GPU_data.writerow([g, p, l])











 





