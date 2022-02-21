import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "*"
news_api_key = "*"
account_sid = "*"
auth_token = "*"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key,
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
articles = news_response.json()["articles"]

three_articles = articles[:3]

difference = yesterday_closing_price - day_before_yesterday_closing_price
change_symbol = None
if difference < 0:
    change_symbol = "🔻"
else:
    change_symbol = "🔺"
positive_difference = abs(difference)
diff_percent = positive_difference / day_before_yesterday_closing_price * 100

formatted_articles = [f"{STOCK}: {change_symbol}{'{:.2f}'.format(diff_percent)}\n" \
                      f"Headline: {article['title']}. \n" \
                      f"Brief: {article['description']}" for article in three_articles]

if diff_percent >= 2:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+*',
            to='+*',
        )
        print(message.status)

# # STEP 1: Use https://newsapi.org/docs/endpoints/everything When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News"). HINT 1: Get the closing price for yesterday and the
# day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive
# difference is 20. HINT 2: Work out the value of 5% of yesterday's closing stock price.


# # STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
