# //scrape website by selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# //import options 

chrome_options = Options()
driver = webdriver.Chrome(options=Options())
chrome_options.add_experimental_option("detach", True)

driver.get("https://www.metroshoes.com.pk/")

driver.maximize_window()
time.sleep(20)


data = driver.xpath("//*[@id='nt_menu_canvas']").click()


time.sleep(40)


