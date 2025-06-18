import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class Price_Scraper:
    def __init__(self):
        pass
    def scrape_price(self):
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        self.max_tries = 5
        self.retries = 0
        while self.retries < self.max_tries:
            try:
                self.url = input(str('Paste it here: '))
                while len(self.url) < 2:
                    self.retries += 1
                    self.url = input(str('Paste it here: '))
                self.lowest_price = input('Enter the lowest price you want to be notified on (just the digits): ')
                web_response = requests.get(url=self.url,headers=header)

                if web_response.status_code != 200 :
                    print('[!]There was an error\n'
                          'Make sure you copied the url properly')
                    self.retries += 1
                    continue

            except requests.RequestException :
                print(requests.RequestException)
                return
            else :
                html_web_data= str(web_response.text)
                self.soup = BeautifulSoup(html_web_data,'html.parser')
                price_text  = self.soup.find(name='span',class_='a-price-whole').text
                self.price_symbol = self.soup.find(name='span',class_='a-price-symbol').text
                self.price= price_text.split(',')[0]
                self.title_ = self.soup.find(name='Title')
                return
        print('Too many attempts made !')
        return

    def price_symbol(self):
        return self.price_symbol
    def item_name(self):
        return self.title_.split(':')[0]
    def price(self):
        return self.price

    def desired_price(self):
        return self.lowest_price
    def how_to_use(self):
        print('How to use:\n'
              '1.Go to amazon\n'
              '2.GO to the item you want to track the price of\n'
              '3.Copy the url of the website {at the very top it starts with "https://www.amazon.co.."\n')

        # self.lowest_target_price = input('Now enter the lowest price you want to be notified on: ')