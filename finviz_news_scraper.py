from concurrent.futures import ThreadPoolExecutor, thread
from multiprocessing.pool import ThreadPool
from posixpath import split
import re
from venv import create
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,ssl
import time
import json
from datetime import datetime
from collections import defaultdict
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re
import threading
import pymongo
import concurrent.futures
import string

max_hits = 1#int(sys.argv[2]) if (len(sys.argv) > 2) else 3
interval = 1#int(sys.argv[3]) if (len(sys.argv) > 3) else 5

chromedriver_path = './chromedriver'

def create_driver():
    
    # options.add_experimental_option('excludeSwitches', [])
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    return driver

def get_news(driver, url = 'https://finviz.com/news.ashx?v=2'):
    driver.get(url)
    driver.refresh()
    time.sleep(2)

    t = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/table[2]/tbody")
    print(t)
    for i in t:
        print(i.link, i.text)



if __name__ == "__main__":
    while True:
        
        driver = create_driver()

        # get news
        news = get_news(driver)

        time.sleep(60)
