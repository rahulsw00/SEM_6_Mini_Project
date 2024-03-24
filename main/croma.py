from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


url = 'https://www.croma.com/searchB?q='
eurl = '%3AtopRated&text'
class croma_scraper:

    def __init__(self, product):
        self.croma_data = []

        for i in range(1):
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            driver.get(url + str(product) + eurl + str(product))
            time.sleep(2)
            soup=bs(driver.page_source,'html.parser')
            names = soup.findAll('h3', attrs={'class': 'plp-prod-title'})
            prices = soup.findAll('span', attrs={'class': 'plp-srp-new-amount'})
            images = soup.findAll('div', attrs={'class': 'product-img plp-card-thumbnail plpnewsearch'})
            refs = soup.findAll('h3', attrs={'class': 'product-title plp-prod-title'})

            for name in names:
                self.croma_data.append(name.text)
                break
            for price in prices:
                self.croma_data.append(price.text)
                break
            for a in images:
                for img in a:
                    self.croma_data.append(img['src'])
                    break
                break
            self.croma_data.append("NA") #rating
            for a in refs:
                for href in a:
                    self.croma_data.append(href['href'])
                    self.croma_data[-1] = 'https://www.croma.com' + self.croma_data[-1]
                    break
                break
        
    def get_lsit(self):
        return self.croma_data
                        