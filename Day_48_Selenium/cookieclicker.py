from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_elements_by_id("cookies")

timer = time.time() + 5
timeout = time.time() + 5*60

while True:
    cookie.click()
    if time.time() > timer:
        timer += 5
        upgrades = driver.find_elements_by_css_selector(".product.unlocked.enabled")
        priciest_upgrade = upgrades[-1]
        priciest_upgrade.click()
    if time.time() > timeout:
        cookies_per_second = driver.find_element_by_css_selector("#cookies div")
        print(cookies_per_second.text)
        break