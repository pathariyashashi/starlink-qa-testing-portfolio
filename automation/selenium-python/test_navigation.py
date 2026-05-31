from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.starlink.com")

time.sleep(3)

nav = driver.find_element(By.TAG_NAME, "nav")

assert nav.is_displayed()

print("Navigation Test Passed")

driver.quit()