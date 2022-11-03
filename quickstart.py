from bs4 import BeautifulSoup
import requests
import csv

page_to_scrap = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page_to_scrap.text, "html.parser")
quotes = soup.findAll("span", attrs={"class" :"text"})
authors = soup.findAll("small", attrs={"class" :"author"})



# create a variable to open a csv file and write    
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

i = 0
for quote, author in zip(quotes , authors):
    print(i, quote.text, author.text )
    i+=1
    writer.writerow([quote.text, author.text])
    
file.close()
    
    
    
