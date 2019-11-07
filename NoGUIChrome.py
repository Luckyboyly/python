from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import redis
#无界面模拟访问
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.baidu.com")
print("")
print(driver.page_source)
