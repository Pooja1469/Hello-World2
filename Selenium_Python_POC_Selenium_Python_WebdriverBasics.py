from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\POOJA\\geckodriver-v0.26.0-win64\\geckodriver.exe")

driver.get("http://www.google.com")
time.sleep(5)
print(driver.title)

driver.find_element_by_name("q").send_keys("Selenium Python")
optionsList = driver.find_elements_by_xpath("//*[@class='erkvQe']/li/span")

print(len(optionsList))
for ele in optionsList:
    print(ele.text)

time.sleep(5)
driver.quit()
