from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://try.requesttracker.io")
elemento1 = driver.find_element(By.ID, "inputName")
elemento1.clear()
elemento1.send_keys("guest")

elemento2 = driver.find_element(By.ID, "inputPassword")
elemento2.clear()
elemento2.send_keys("guest")

driver.find_element(By.ID, "submit").click()

time.sleep(20)

driver.close()
