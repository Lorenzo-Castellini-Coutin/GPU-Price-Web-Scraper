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

GPUs = soup.find_all('div', {'class' : 'item-container'})

prices = soup.find_all('strong')



