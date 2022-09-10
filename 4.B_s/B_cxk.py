import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By    #Because of This version of selenium, it should imports 'By' rather than 'BY'
from selenium.webdriver.common.action_chains import ActionChains as AC


browser=webdriver.Edge('D:\edgedriver_win64\msedgedriver.exe')
browser.get("https://www.bilibili.com/")
time.sleep(2)

browser.find_element(By.CLASS_NAME,'nav-search-input').send_keys('蔡徐坤 篮球')
time.sleep(2)

button=browser.find_element(By.CLASS_NAME,'nav-search-btn')
button.click()

#此时跳转到搜索后的页面



