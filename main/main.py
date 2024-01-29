import requests
from bs4 import BeautifulSoup
import pandas as pandas 
import time

#creating URL from the input for different shopping websites
prod = input("What product do you want to search: ")
i = 0
prod_list = prod.split()
print(prod_list)
newprod = " "
for i in range(len(prod_list)):
    newprod = newprod + prod_list[i] + "+"
    #URL = URL + newprod

URL_Amazon = "https://www.amazon.in/s?k=" + newprod
URL_Flipkart = "https://www.flipkart.com/search?q=" + newprod
print(URL_Amazon)

