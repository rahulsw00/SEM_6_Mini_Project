import requests
from bs4 import BeautifulSoup
import pandas as pandas 
import time

#creating URL from the input for different shopping websites
prod = input("What product do you want to search: ")

prod_list = prod.split()
URL = ""
for i in prod_list:
    URL = URL + i + "+"

URL_Amazon = "https://www.amazon.in/s?k=" + URL
URL_Flipkart = "https://www.flipkart.com/search?q=" + URL + '&sort=relevance'
print(URL_Flipkart)

headers = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36'}

page = requests.get(URL_Flipkart, headers= headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()

top_flexbox = soup.find('div', class_ = '_13oc-S')

print(top_flexbox.prettify())
top_info = top_flexbox.select_one('img')
top_price = top_flexbox.select('div', class_ = '_30jeq3')
print(top_price)
#print(top_info)
alt = top_info.get('alt')
src = top_info.get('src')
print(alt, src)
