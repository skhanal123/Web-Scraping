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
        url = f'http://api.scraperapi.com?api_key=2a0be443580639b2aca4850cac31c7ab&url=https://www.amazon.in/product-reviews/{asin}/ref=cm_cr_arp_d_paging_btm_next_{i}?ie=UTF8&reviewerType=all_reviews&pageNumber={i}'
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
            
        #     connection = mysql.connector.connect(
        #     host = "localhost",
        #     user = "root",
        #     password = "suman@123",
        #     database = "scraping"
        #     )
        #     print(connection)
        #     query = """INSERT INTO bestrank (rank1, title, rating, no_of_rating, price) 
        #                             VALUES 
        #                             (%s,%s,%s,%s,%s) """

        #     record = (rank_f, title_f, rating_f, No_of_ratings_f, Price_f)

        #     cursor = connection.cursor()
        #     cursor.execute(query, record)
        #     connection.commit()
        #     print(cursor.rowcount, "Record inserted successfully into bestrank table")
                
        










# from requests_html import HTMLSession
# from scraper_api import ScraperAPIClient
# import json
# import time
# import pandas as pd

# headers = {
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
# }

# page_number = [2]
# all_products =[]
# for i in page_number:
#     s = HTMLSession()
#     r = s.get(f'http://api.scraperapi.com?api_key=2a0be443580639b2aca4850cac31c7ab&url=https://www.amazon.in/gp/bestsellers/kitchen/1380032031/ref=zg_bs_pg_2?ie=UTF8&pg={i}', headers=headers)
#     r.html.render(timeout=1000)
#     items = r.html.find('div[class=p13n-desktop-grid]')
#     print(items[0])
    
#     for item in items:
#         print(item)
#         try:
#             rank = item.find('span[class=zg-badge-text]', first = True).text
#         except:
#             rank = "No rank found"
#         print(rank)
        
#         try:
#             product_link = item.find('a[class=a-link-normal]', first = True).attrs['href']
#         except:
#             product_link = "No product link found"
#         print(product_link)
        
#         try:
#             asin = product_link.split('/')[3]
#         except:
#             asin = "No asin found"
#         print(asin)
        
#         try:
#             product_title = item.find('div[class=p13n-sc-truncated]', first = True).text
#         except:
#             product_title = "No title found"
#         print(product_title)
        
#         try:
#             rating = item.find('span[class=a-icon-alt]', first = True).text
#         except:
#             rating = "No rating found"
#         print(rating)
        
#         product ={
#             'rank': rank,
#             'product_link': product_link,
#             'asin': asin,
#             'title': product_title,
#             'rating': rating
#         }

#         all_products.append(product)

# final_details = pd.DataFrame(all_products)
# final_details.to_csv('C:/Users/Suman Khanal/Downloads/rank_test1.csv')



