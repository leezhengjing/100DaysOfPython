from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import os
from time import sleep

CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
SERVICE = Service(CHROME_DRIVER_PATH)
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(1)
        username_field = self.driver.find_element(by=By.NAME, value="username")
        username_field.send_keys(USERNAME)
        password_field = self.driver.find_element(by=By.NAME, value="password")
        password_field.send_keys(PASSWORD)
        sleep(1)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

    def find_followers(self):
        sleep(3)
        self.driver.get("https://www.instagram.com/chefsteps/")
        followers = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/section/main/div/header/section/ul/li['
                                                   '2]/a/div')
        followers.click()
        for n in range(10):
            sleep(2)
            pop_up = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]//a')
            pop_up.send_keys(Keys.END)
        sleep(1)
        pop_up = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]//a')
        pop_up.send_keys(Keys.HOME)

    def follow(self):
        sleep(1)
        buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='li button')
        print(buttons)
        for button in buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/div/div/div['
                                                                            '3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
