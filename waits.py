from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from icecream import ic

driver = webdriver.Chrome('/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

ic(driver.title)
ic(driver.current_url)

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('b')
items = driver.find_elements(By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div[1]/img')
print(items)


time.sleep(2)

driver.close()


