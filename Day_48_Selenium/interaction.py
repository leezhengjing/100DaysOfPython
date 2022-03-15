from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = "C:\Development\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Lee")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Zheng Jing")

email_address = driver.find_element_by_name("email")
email_address.send_keys("codingwithzeejae@gmail.com")

sign_up = driver.find_element_by_css_selector("form button")
sign_up.click()
