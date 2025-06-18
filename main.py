import email_sender
import scraper
from scraper import Price_Scraper
from email_sender import *
amazon_price_scraper = scraper.Price_Scraper()
amazon_price_scraper.how_to_use()
amazon_price_scraper.scrape_price()
email = email_sender.Email()
email.send_mail()