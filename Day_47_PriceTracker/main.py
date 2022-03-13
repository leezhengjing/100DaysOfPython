from bs4 import BeautifulSoup
import requests
import smtplib
import os

URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG/ref=psdc_289940_t1_B08PQ2KWHS"

headers = {
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

r = requests.get(url=URL, headers=headers)

amazon_webpage = r.text
soup = BeautifulSoup(amazon_webpage, 'lxml')
price_element = soup.find(name="span", class_="a-offscreen")
price = float(price_element.text[1:])
title_element = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
title = title_element.text.strip()


MY_GMAIL = os.environ["MY_GMAIL"]
GMAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]
ADDRESS = os.environ["ADDRESS"]

message = f"{title} is now ${price}\n{URL}"
print(message)

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL,
            to_addrs=ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )