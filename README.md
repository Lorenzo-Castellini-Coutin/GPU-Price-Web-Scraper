## GPU Price Web Scraper

### Introduction & Project Scope
This Python script scrapes the Newegg.com website, specifically the RTX 4070 listings within Newegg.com, in order to obtain information on the diverse models, prices, and links with regards to the RTX 4070 GPUs available at Newegg.com. All of this information is then organized in columns and exported as a csv file. The csv file can help a user analyze the diverse listings of models of RTX 4070 GPUs in order to take an informed decision when it comes to purchasing one for their computer.

![image](https://github.com/Lorenzo-Castellini-Coutin/GPU-Price-Web-Scraper/assets/153740191/dc77fd03-5bbb-4a57-abbb-6368f1b39a39)
_This is an example of the first results of the CSV file produced by the script._

### How does it all work?
The script uses the BeautifulSoup library, alongside the selenium library in order to scrape the website's information in an automated format. The user can specify the amount of pages the script will scrape data from. Furthermore, it uses the pyshorteners library to shorten the buy now links provided by Newegg.com. Finally, it uses the csv library in order to export said data as a csv file.

### Usage
In order to run this script locally on your machine, you can clone this repo. Make sure you have all of the libraries used in the code, installed in your machine. Furthermore, the user must specify the amount of pages the script will scrape the info within the website, through the terminal. Lastly, this script is only compatible with Chrome browsers.

### Advisory on Usage
This script is designed to only extract data, and is not intended for other purposes which might violate the site's terms of service. Furthermore, make sure to read the license found in this repository before usage/taking any actions.

### Additional Notes
This script can be used for any other GPU model or item within the Newegg.com website, by changing the base url, and some other few aspects. Furthermore, this project was developed for educative purposes, and it is not intended to be used in such a way that violates laws/policies. Lastly, any feedback with regards to this project is greatly appreciated. 
