import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree

url = 'https://www.metroshoes.com.pk/collections/new-in'
proxy_ip_port  = '168.100.130.128:8080'
result = requests.get(url)
result2 = result.text


file = open('Price.csv', 'w')
file_data = csv.writer(file)

file_data.writerow(['Name', 'Price'])


# get from xpath

soup = BeautifulSoup(result2, "html.parser")

dom = etree.HTML(str(soup))

res = dom.xpath("//*[@class='cd chp']")
price = dom.xpath("//*[@class='money']")


j = 0
for i, k in list(zip(res, price)):
    print(j, i.text, k.text)
    file_data.writerow([i.text, k.text])
    
    j += 1


# soup = BeautifulSoup(result2, "html.parser")
# file = open('data.csv', 'w')
# file_data = csv.writer(file)

# file_data.writerow(['LINKS'])

# data = soup.find_all('a')

# for i in data:
#     file_data.writerow(["https://www.metroshoes.com.pk" + i.get('href')])
#     print(i.get('href'))
