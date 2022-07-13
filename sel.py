from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get('https://google.com')
assert 'Google' in driver.title
elem = driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys('francisco magot')
elem.send_keys(Keys.RETURN)