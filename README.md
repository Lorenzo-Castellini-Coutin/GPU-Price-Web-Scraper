## GPU Price Scraper
### Introduction
This Python script scrapes the Newegg website, specifically the RTX 4070 GPU shop link, in order to obtain information on the diverse models, prices, and links with regards to the RTX 4070 GPUs available at Newegg.com. All of this information is then organized in columns and exported as a csv file. 

![Screenshot 2024-06-03 135805](https://github.com/Lorenzo-Castellini-Coutin/GPU-Price-Scraper/assets/153740191/e1357a4c-5489-4400-bec3-99cc30e93fe3)


### How it works?
The script uses the BeautifulSoup library, alongside the selenium library in order to scrape the website's information in an automated format. The user can specify the amount of pages the script will scrape data from. Furthermore, it uses the pyshorteners library to shorten the buy now links provided by Newegg.com. Finally, it uses the csv library in order to export said data as a csv file.

### Usage
In order to run this script locally on your machine, make sure you have all of the libraries used installed in your machine. Furthermore, the user must specify the amount of pages the script will scrape the info within the website, through the terminal. Furthemore, this script is only compatible with Chrome browsers.
### Advisory
This script is designed to only extract data, and is not intended for other purposes which might violate the site's terms of service.
