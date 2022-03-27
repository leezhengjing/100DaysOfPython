from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time


GOOGLE_SHEETS = "https://docs.google.com/forms/d/e/1FAIpQLSe3KtE80Y7Fk5kH1FIVo9KHp4dbLOzfEg53n-1ZxkMQ2zFnQw/viewform" \
                "?usp=sf_link"



headers = {
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

response = requests.get(url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.49431383642042%2C%22east%22%3A-122.33999025853956%2C%22south%22%3A37.71271146018368%2C%22north%22%3A37.82018636737101%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",
                        headers=headers)
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, "html.parser")
print(soup.text)
prices = soup.find_all(name="div", class_="list-card-price")
price_list = [price.text.split('/')[0].split('+')[0] for price in prices]
print(price_list)
print(len(price_list))
links = soup.find_all(name="a", class_="list-card-link")
link_list = [link.get("href") for link in links]
link_list = link_list[::2]
for index in range(len(link_list)):
    if len(link_list[index]) < 60:
        new_link = f"https://www.zillow.com{link_list[index]}"
        link_list[index] = new_link
print(link_list)
print(len(link_list))

addresses = soup.find_all(name="address", class_="list-card-addr")
address_list = [address.text for address in addresses]
print(address_list)
print(len(address_list))


CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
SERVICE = Service(CHROME_DRIVER_PATH)


class FormBot:
    def __init__(self, addresses, prices, links):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.addresses = addresses
        self.prices = prices
        self.links = links
        for n in range(len(addresses)):
            self.fill_forms(n)

    def fill_forms(self, n):
        self.driver.get(GOOGLE_SHEETS)
        first_question = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                     '1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        first_question.send_keys(self.addresses[n])
        second_question = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                      '2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        second_question.send_keys(self.prices[n])
        third_question = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                     '3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        third_question.send_keys(self.links[n])
        time.sleep(1)
        submit_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div['
                                                                    '1]/div/span/span')
        submit_button.click()


bot = FormBot(address_list, price_list, link_list)
