#Author: Lorenzo Castellini Coutin

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import csv
import pyshorteners

Basic_URL = 'https://www.newegg.com/p/pl?N=100007709&d=rtx%204070&isdeptsrh=1' #Newegg URL for RTX 4070 GPU

num_of_pages = int(input('Please enter the number of pages you want to search in Newegg: '))

def web_scrape(Basic_URL, num_of_pages):
    driver = webdriver.Chrome()
    GPU_list = []
    base_prices_list = []
    shop_links_list = []

    web = requests.get('https://www.newegg.com/p/pl?N=100007709&d=rtx%204070&isdeptsrh=1')
    if web.status_code == 200:
        for pages in range(1, num_of_pages + 1):
            pages_url = f'https://www.newegg.com/p/pl?N=100007709&d=rtx%204070&isdeptsrh={pages}'
            driver.get(pages_url)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            GPUs = soup.find_all('a', {'class' : 'item-title'})

            for g in GPUs:
                GPU_list.append(g.get_text())

            base_prices = soup.find_all('li', {'class' : 'price-current'})

            for p in base_prices:
                price_tag = p.find('strong')

                if price_tag:
                    base_prices_list.append("$" + str(price_tag.get_text()))

            shop_links = soup.find_all('a', {'class' : 'item-title'})

            for l in shop_links:
                full_links = l.get('href')
                shortener = pyshorteners.Shortener()
                short_links = shortener.tinyurl.short(full_links)
                shop_links_list.append(short_links)

    else:
        print('The website you are trying to access is not available. Try again later.')
    
    file_path = 'GPU_Scrapped_Data.csv'
    
    with open(file_path, 'a', newline = '') as csv_file:
        GPU_data = csv.writer(csv_file)
        GPU_data.writerow(['Item Information', 'Base Price (Shipping not included)', 'Newegg Purchase Link'])

        for g, p, l in zip(GPU_list, base_prices_list, shop_links_list):
            GPU_data.writerow([g, p, l])

web_scrape(Basic_URL, num_of_pages)


#Author: Lorenzo Castellini Coutin





 





