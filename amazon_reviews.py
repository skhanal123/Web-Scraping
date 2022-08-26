import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import mysql.connector

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

page_number = [1,2]
all_products =[]
asins = ['B00JFUD1XO']
for asin in asins: 
    for i in page_number:
        url = f'http://api.scraperapi.com?api_key=**************************&url=https://www.amazon.in/product-reviews/{asin}/ref=cm_cr_arp_d_paging_btm_next_{i}?ie=UTF8&reviewerType=all_reviews&pageNumber={i}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser') 
        a = soup.find_all("div", class_="aok-relative")
        print(len(a))

        for i in a:
            asin1 = asin
            try:
                rating = i.find('span', class_="a-icon-alt")
                rating_f = rating.text
            except:
                rating_f = "Rating not found"
            try:
                title = i.find('a', class_="review-title-content").find('span')
                title_f = title.text
            except:
                title_f = "Title not found"
            try:
                date = i.find('span', class_="review-date")
                date_f = date.text
            except:
                date_f = "Date not found"
            try:
                review = i.find('span', class_="review-text-content").find('span')
                review_f = review.text
            except:
                review_f = "Review not found"
            
            
            print(asin, rating_f, title_f, date_f, review_f)




