from requests_html import HTMLSession
from scraper_api import ScraperAPIClient
import json
import time

client = ScraperAPIClient('XXXXXXXXXXXX')


s = HTMLSession()

asins = ['B07W4V11P9','B08SM7K1PJ']

for asin in asins:
    r = s.get(f'http://api.scraperapi.com?api_key=XXXXXXXXXXXXXXX&url=https://www.amazon.in/dp/{asin}')
    try:
        title = r.html.xpath('//*[@id="productTitle"]', first=True).text.strip()
    except:
        title= "Title not found"
    try:
        price = r.html.find('span[class=a-offscreen]', first=True).text.strip()
    except:
        price = "No price found"
    
    try:
        buybox = r.html.xpath('//*[@id="merchant-info"]/a[1]/span', first=True).text.strip()
    except:
        buybox = "Seller not found"

    print(title, price, buybox)
