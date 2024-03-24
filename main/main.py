import pandas as pd
from flipkart import flipkart_scraper
from croma import croma_scraper


top_img = []
top_name = []
top_price = []
top_rate = []
top_ref = []

product = input("Enter product name: ")


def data(top_name, top_price, top_img, top_rate, top_ref):
    df = pd.DataFrame()
    df['Name'] = top_name
    df['Price'] = top_price
    df['Image'] = top_img
    df['Rating'] = top_rate
    df['Href'] = top_ref
    print("Scrapping Done.......... ")
    print(df)

class FlipClass:
    def __init__(self):
        self.flip_instance = flipkart_scraper(product)
    
    def get_list_from_flipkart(self):
        return self.flip_instance.get_list()
    
class CromaClass:
    def __init__(self):
        self.croma_instance = croma_scraper(product)

    def get_list_from_croma(self):
        return self.croma_instance.get_lsit() 

if __name__ == "__main__":
    croma_instance = CromaClass()
    flip_instance = FlipClass()
    flipkart_data = flip_instance.get_list_from_flipkart()
    croma_data = croma_instance.get_list_from_croma()
    print(flipkart_data)
    print(croma_data)
