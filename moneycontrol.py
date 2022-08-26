import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://api.scraperapi.com?***api_key=XXXXXXXXXXXab&url=https:XXX//www.moneycontrol.com/india/stockpricequote/"

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;**** x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
  'accept-language': 'en-US,en;q=0.9****',
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

company_table = soup.find('table', class_ ='pcq_tbl MT10')



final = []

rows = company_table.find_all('tr')

for row in rows[1:]:
    tds = row.find_all('td')
    for td in tds:
        links = td.find('a')

        final.append(links.attrs['href'])


company_list = pd.DataFrame(final)
company_list.to_csv('C:/Users/Suman Khanal/Downloads/company_list.csv')


