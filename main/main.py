import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests

page_range = (1)
top_img = []
top_name = []
top_price = []

product = input("Enter product name: ")

url = 'https://www.flipkart.com/search?q='
eurl = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='


class webscreapping:

    def __init__(self, url):

        for page in range(page_range):
            r = requests.get(url + str(product) + eurl + str(page))
            data = r.content
            soup = BeautifulSoup(data, "html.parser") 
            names = soup.findAll('div', attrs={'class': '_4rR01T'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3 _1_WHN1'})
            images = soup.findAll('img', attrs={'class': '_396cs4'})
            for name in names:
                top_name.append(name.text)
                break
            for price in prices:
                top_price.append(price.text)
                break
            for img in images:
                top_img.append(img)
                break
            break

def data(top_name, top_price, top_img):
    df = pd.DataFrame()
    df['Name'] = top_name
    df['Price'] = top_price
    df['Image'] = top_img
    print("Scrapping Done.......... ")
    print(df)


ws1 = webscreapping(url)
data(top_name, top_price, top_img)

