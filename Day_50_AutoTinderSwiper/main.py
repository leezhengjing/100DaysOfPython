from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os

FACEBOOK_USERNAME = os.environ["FACEBOOK_USERNAME"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]


chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
ser = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser)
driver.get("https://tinder.com/")

time.sleep(1)

log_in = driver.find_element_by_xpath('//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(1)

log_in_with_facebook = driver.find_element_by_xpath('//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button')
log_in_with_facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(1)

fb_email_address = driver.find_element_by_name("email")
fb_email_address.send_keys(FACEBOOK_USERNAME)
fb_password = driver.find_element_by_name("pass")
fb_password.send_keys(FACEBOOK_PASSWORD)
fb_login = driver.find_element_by_name("login")
fb_login.click()

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

allow_location = driver.find_element_by_xpath('//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(2)

notifications = driver.find_element_by_xpath('//*[@id="t492665908"]/div/div/div/div/div[3]/button[2]')
notifications.click()

time.sleep(2)

xpath_cookies = driver.find_element_by_xpath('//*[@id="t-2073920312"]/div/div[2]/div/div/div[1]/div[1]/button')
xpath_cookies.click()

for n in range(100):
    time.sleep(2)
    try:
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()