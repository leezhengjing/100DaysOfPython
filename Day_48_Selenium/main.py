from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu li")
event_list = [event.text.split("\n") for event in events]
event_list_of_dicts = [{'time': item[0], 'name': item[1]} for item in event_list]
event_data = {index: event_list_of_dicts[index] for index in range(len(event_list_of_dicts))}
print(event_data)

# driver.close()
driver.quit()
