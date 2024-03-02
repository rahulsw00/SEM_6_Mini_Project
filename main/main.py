import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests

page_range = (1)
top_img = []
top_name = []
top_price = []
top_rate = []
top_ref = []
product = input("Enter product name: ")

url = 'https://www.flipkart.com/search?q='
eurl = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='


class scraper:

    def __init__(self, url):

        for page in range(page_range):
            r = requests.get(url + str(product) + eurl + str(page))
            data = r.content
            soup = BeautifulSoup(data, "html.parser") 
            names = soup.findAll('div', attrs={'class': '_4rR01T'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3 _1_WHN1'})
            images = soup.findAll('img', attrs={'class': '_396cs4'})
            ratings = soup.findAll('div', attrs={'class': '_3LWZlK'})
            refs = soup.findAll('a', attrs={'class': '_1fQZEK'})
            for name in names:
                top_name.append(name.text)
                break
            for price in prices:
                top_price.append(price.text)
                break
            for img in images:
                top_img.append(img['src'])
                break
            for rate in ratings:
                top_rate.append(rate.text)
                break
            for href in refs:
                top_ref.append(href['href'])
                break
            break

def data(top_name, top_price, top_img, top_rate, top_ref):
    df = pd.DataFrame()
    df['Name'] = top_name
    df['Price'] = top_price
    df['Image'] = top_img
    df['Rating'] = top_rate
    df['Href'] = top_ref
    print("Scrapping Done.......... ")
    print(df)


scraper(url)
data(top_name, top_price, top_img, top_rate, top_ref)

