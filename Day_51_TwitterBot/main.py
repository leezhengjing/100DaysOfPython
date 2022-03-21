import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 125
PROMISED_UP = 125
CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
SERVICE = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element_by_class_name("upload-speed").text
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")
        time.sleep(1)
        sign_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in_button.click()
        time.sleep(1)
        email_input = self.driver.find_element_by_name("text")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_button.click()
        time.sleep(1)
        try:
            confirm_human = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        except NoSuchElementException:
            pass
        else:
            confirm_human.send_keys('LeeZhengJing1')
            time.sleep(1)
            confirm_human_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            confirm_human_button.click()
        time.sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        log_in_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        log_in_button.click()
        time.sleep(1)
        twitter_entry = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div')
        twitter_entry.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 1Gbps?")
        time.sleep(1)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
