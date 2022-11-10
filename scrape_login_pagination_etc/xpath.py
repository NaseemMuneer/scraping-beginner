import requests
from bs4 import BeautifulSoup
from lxml import etree


url = 'https://firstround.com/companies/'

web_to_scrape = requests.get(url)

soup = BeautifulSoup(web_to_scrape.content, "html.parser")
dom = etree.HTML(str(soup))
res = (dom.xpath('//*[@class = "container"]/div/child::h1'))

for i in res:
    print(i.text)


# print(web_to_scrape.text, "html.parser")

# header = soup.find("div", attrs={"class":"intro-text-block"})
# print(header.text)

