from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2966803033&f_E=2&f_JT=P&geoId=102454443&keywords=cashier&location=Singapore&sortBy=R")

sleep(3)
sign_in_first = driver.find_element_by_class_name("cta-modal__primary-btn")
sign_in_first.click()

sleep(3)
email = driver.find_element_by_name("session_key")
email.send_keys(EMAIL)

password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)

sleep(0.5)
sign_in_second = driver.find_element_by_css_selector(".btn__primary--large.from__button--floating")
sign_in_second.click()

sleep(1)
all_jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

for job in all_jobs:
    job.click()
    sleep(1)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    sleep(1)

