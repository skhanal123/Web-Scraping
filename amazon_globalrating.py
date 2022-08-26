from requests_html import HTMLSession
from scraper_api import ScraperAPIClient
import json
import time
import sqlite3
import pandas as pd
from retry import retry

conn = sqlite3.connect('globalrating.db')
c = conn.cursor()

c.execute('''DROP TABLE flatbedsheets''')
c.execute('''CREATE TABLE flatbedsheets(asin TEXT, globalrating TEXT)''')


s = HTMLSession()
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# asins = [
#     'B09BJY3GC3'
# ]
asins = [
    'B09BJY3GC3','B01LX16EDU','B09J2G9PMZ','B07H8GV5ZC','B09BJY4GY8','B09HC9SR3T','B08XMLHXV6','B08XVMD3JN','B095PQDZJS','B08Z8MVS6D','B089B3GV6N','B09JZVZJPL','B08HJZBN39','B0981D48NP','B09797QHJ5','B085MXSB1X','B08461V5X1','B095PPRRDD','B095PMMN97','B09CTWH3TP','B08SHJ56SQ','B09BK1FVXC','B09778DHLB','B01N79JFLW','B08Y74J31H','B0977BQWXQ','B09JLSVZ2Y','B09LR5M5ZJ','B078YM1744','B092MR7QWF','B08Z9N6GPV','B01GOCURNW','B092J5QNFW','B08RZ47MJ9','B09491PCY7','B095PQJVBT','B09CTY8WHC','B01LZMXQI7','B07MKCWS8Q','B01C49HK70','B08XM3BSR7','B08X9WWF7K','B098PKCXNR','B09BJZ3VWS','B09CTX9MW2','B08Y2J2N4L','B095PL85ND','B01J24OWI0','B01DE6Z2R2','B08WHF4PPD','B084GYVBDH','B08X4XXYWP','B098MQ5Q53','B09583L55F','B09HPYG2LS','B09LR4XJMP','B09KL26LNW','B09LR3F6S8','B09M9VDZ8R','B09BJZK3WB','B09M9W73KS','B09J2D8N81','B09GB91JF9','B08MCNRGYP','B08LVN3KY5'
]

@ retry()
def geturl(asin):
    r = s.get(f'http://api.scraperapi.com?api_key=***************************&url=https://www.amazon.in/product-reviews/{asin}', headers=headers)
    r.html.render(timeout=1000)
    time.sleep(1)
    return r

data = []
for asin in asins:
    r = geturl(asin)    
    try:
        global_rating = r.html.find('#filter-info-section > div > span', first=True).text.strip()
    except:
        global_rating = "No rating found"

    asin = asin

    print(asins.index(asin), asin, global_rating)

    c.execute('''INSERT INTO flatbedsheets VALUES(?,?)''', (asin, global_rating))

conn.commit()
print('complete.')

c.execute('''SELECT * FROM flatbedsheets''')
results = c.fetchall()

final_data = pd.DataFrame(results)
final_data.to_csv('C:/Users/Suman Khanal/Downloads/try1.csv')

