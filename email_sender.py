import os
import smtplib
from dotenv import load_dotenv

import scraper
from scraper import Price_Scraper

class Email:
    def __init__(self):
        amazon_price_scraper = scraper.Price_Scraper()
        self.price = amazon_price_scraper.price()
        title = amazon_price_scraper.item_name()
        symbol = amazon_price_scraper.price_symbol()
        self.lowest_price = amazon_price_scraper.lowest_price()
        url = amazon_price_scraper.url

        self.email = os.getenv('email')
        self.body = f"""
            {title}
            The price has dropped to {symbol}{self.lowest_price}
    
            Purchase now :{url}
        """
    def send_mail(self):
        if self.price <= self.lowest_price:
            with smtplib.SMTP(os.environ.get('smtp_server')) as email_connection :
                email_connection.starttls()
                email_connection.login(user = self.email,password=os.getenv('email_app_password'))
                email_connection.sendmail(msg=f'Subject:Amazon price tracker\n\n{self.body}',to_addrs='',from_addr=self.email)

        else:
            print('Price has not dropped yet')