from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy , ProxyType 
import time


proxy_ip_port  = '45.167.125.97:9992'

url = 'https://www.whatismyipaddress.com'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)
driver.get(url)

driver.maximize_window()
time.sleep(80)

driver.quit()
