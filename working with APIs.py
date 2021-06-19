'''
Web automation using APIs in python

'''


!pip install selenium
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os

driver = webdriver.Chrome('C:/Users/212592107/Downloads/chromedriver.exe')
driver.get('https://www.xxx.com/home');
time.sleep(2) # A wait to load the page completely
input_ = driver.find_element_by_xpath('//*[@id="mat-input-0"]')  
input_.send_keys('xxxx')
input_ = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/div[1]/div/div/button')
input_.click()
input_ = driver.find_element_by_name('Free')
input_.click()

# to be continued ! 
