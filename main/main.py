import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

empty = np.full((3), 'NaN')
product = input("Enter product name: ")
dic = {'Name': empty, 'Price': empty, 'Image': empty, 'Link': empty}
df = pd.DataFrame(dic)

class FlipClass:
    def __init__(self, product):   
        url = 'https://www.flipkart.com/search?q='
        eurl = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

        r = requests.get(url + str(product) + eurl)
        data = r.content
        soup = bs(data, "html.parser") 
        div = soup.findAll('div', attrs={'class': '_13oc-S'})
        for layout in div:
            sty = layout.div['style']
            break
        if (sty == 'width:25%'):
            names = soup.findAll('a', attrs={'class': 's1Q9rs'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3'})
            images = soup.findAll('img', attrs={'class': '_396cs4'})
            refs = soup.findAll('a', attrs={'class': 's1Q9rs'})
        else:
            names = soup.findAll('div', attrs={'class': '_4rR01T'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3 _1_WHN1'})
            images = soup.findAll('img', attrs={'class': '_396cs4'})
            refs = soup.findAll('a', attrs={'class': '_1fQZEK'})
        for name in names:
            df.loc[0, 'Name'] = name.text
            break
        for price in prices:
            df.loc[0, 'Price'] = price.text
            break
        for img in images:
            df.loc[0, 'Image'] = img['src']
            break
        for href in refs:
            df.loc[0,'Link'] = 'https://www.flipkart.com' + href['href']
            break

class CromaClass:
    def __init__(self, product):
        url = 'https://www.croma.com/searchB?q='
        eurl = '%3AtopRated&text'
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url + str(product) + eurl + str(product))
        time.sleep(1)
        soup=bs(driver.page_source,'html.parser')
        names = soup.findAll('h3', attrs={'class': 'plp-prod-title'})
        prices = soup.findAll('span', attrs={'class': 'plp-srp-new-amount'})
        images = soup.findAll('div', attrs={'class': 'product-img plp-card-thumbnail plpnewsearch'})
        refs = soup.findAll('h3', attrs={'class': 'product-title plp-prod-title'})

        for name in names:
            df.loc[1, 'Name'] = name.text
            break
        for price in prices:
            df.loc[1, 'Price'] = price.text
            break
        for a in images:
            for img in a:
                df.loc[1, 'Image'] = img['src']
                break
            break
        for a in names:
            for href in a:
                df.loc[1,'Link'] = 'https://www.croma.com' + href['href']
                break

class JioClass:
    def __init__(self,product):
        url = "https://www.jiomart.com/search/"
        #eurl = "/in/prod_mart_master_vertical"


        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url + str(product) )
        time.sleep(1)
        soup=bs(driver.page_source,'html.parser')
        names = soup.findAll('div', attrs={'class': 'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})
        prices = soup.findAll('span', attrs={'class': 'jm-heading-xxs jm-mb-xxs'})
        images = soup.findAll('img', attrs={'class': 'lazyautosizes lazyloaded'})
        refs = soup.findAll('a', attrs={'class': 'plp-card-wrapper plp_product_list'})
        for name in names:
            df.loc[2, 'Name'] = name.text
            break
        for price in prices:
            df.loc[2, 'Price'] = price.text
            break
        for img in images:
            df.loc[2, 'Image'] = img['src']
            break
        for href in refs:
            df.loc[2,'Link'] = 'https://www.jiomart.com/' + href['href']
            break

FlipClass(product)
CromaClass(product)
#JioClass(product)

print(df)
