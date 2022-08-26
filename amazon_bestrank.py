import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
import mysql.connector

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

node = 8641218031
page_number = [1,2]
all_products =[]

for i in page_number:
    url = f'http://api.scraperapi.com?api_key=************************&url=https://www.amazon.in/gp/bestsellers/kitchen/{node}/ref=zg_bs_pg_{i}?ie=UTF8&pg={i}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser') 
    a = soup.find_all("div", id="gridItemRoot")
    print(len(a))

    for i in a:
        rank = i.find('span', class_="zg-bdg-text")
        rank_f = rank.text
        try:
            title = i.find('div', class_='_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1')
            title_f = title.text
        except:
            try:
                title = i.find('div', class_='_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc')
                title_f = title.text
            except:
                try:
                    title = i.find('div', class_='_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-5__2l-dX')
                    title_f = title.text
                except:
                    title_f = "Title not found"
        try:
            rating = i.find("span", class_="a-icon-alt")
            rating_f= rating.text
        except:
            rating_f= "Rating not found"
        
        try:
            No_of_ratings = i.find("span", class_="a-size-small")
            No_of_ratings_f = No_of_ratings.text
        except:
            No_of_ratings_f = "No_of_ratings not found"
        try:
            Price = i.find("span", class_="_p13n-zg-list-grid-desktop_price_p13n-sc-price__3mJ9Z")
            Price_f = Price.text
        except:
            Price_f = "Price not found"
        
        print(rank_f, title_f, rating_f, No_of_ratings_f, Price_f)
        
        connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "suman@123",
        database = "scraping"
        )
        print(connection)
        query = """INSERT INTO bestrank (rank1, title, rating, no_of_rating, price) 
                                VALUES 
                                (%s,%s,%s,%s,%s) """

        record = (rank_f, title_f, rating_f, No_of_ratings_f, Price_f)

        cursor = connection.cursor()
        cursor.execute(query, record)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into bestrank table")
