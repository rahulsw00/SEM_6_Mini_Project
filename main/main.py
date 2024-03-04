import pandas as pd
from flipkart import flipkart_scraper


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

class MainClass:
    def __init__(self):
        self.flip_instance = flipkart_scraper(product)

    def get_list_from_flipkart(self):
        return self.flip_instance.get_list()

if __name__ == "__main__":
    main_instance = MainClass()
    flipkart_data = main_instance.get_list_from_flipkart()
    print(flipkart_data)
