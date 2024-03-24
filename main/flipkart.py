from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q='
eurl = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

class flipkart_scraper:

    def __init__(self, product):   
        self.flipkart_data = []

        for i in range(1):
            r = requests.get(url + str(product) + eurl)
            data = r.content
            soup = BeautifulSoup(data, "html.parser") 
            names = soup.findAll('div', attrs={'class': '_4rR01T'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3 _1_WHN1'})
            images = soup.findAll('img', attrs={'class': '_396cs4'})
            ratings = soup.findAll('div', attrs={'class': '_3LWZlK'})
            refs = soup.findAll('a', attrs={'class': '_1fQZEK'})
            for name in names:
                self.flipkart_data.append(name.text)
                break
            for price in prices:
                self.flipkart_data.append(price.text)
                break
            for img in images:
                self.flipkart_data.append(img['src'])
                break
            for rate in ratings:
                self.flipkart_data.append(rate.text)
                break
            for href in refs:
                self.flipkart_data.append(href['href'])
                self.flipkart_data[-1] = 'https://www.flipkart.com/' + self.flipkart_data[-1]
                break
            break
        
    def get_list(self):
        return self.flipkart_data  
