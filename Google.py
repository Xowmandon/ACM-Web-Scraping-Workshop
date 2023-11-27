import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!


#Finds the Search Box, waits until it is Clickable 
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//textarea[@id='APjFqb']")))

#Simulates typing/entering info
search_box.send_keys('ChromeDriver')

#Submits to the field (enter button)
search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()