
import datetime as dt
from dotenv import load_dotenv
import requests
import os 
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def send_sms():
    articles = news.get("articles", [])
    for new in range(min(3, len(articles))):
        news_url = articles[new]["url"]
        news_content = articles[new]["content"]
        news_title = articles[new]["title"]

        if company_percent_change >= 0:
            body_sms = f"{COMPANY_NAME}:🔺{company_percent_change:.2f}% \n{news_title}\n{news_url}"
        else:
            body_sms = f"{COMPANY_NAME}:🔻{company_percent_change:.2f}% \n{news_title}\n{news_url}"

        # SEND SMS
        client = Client(acount_sid, auth_token)
        message = client.messages.create(
            body=body_sms,
            from_="+13612668748",
            to="+573023660773",
        ) 
        print(message.body)

load_dotenv()

# Twilio personal data 
# acount_sid = os.getenv("TWILIO_SID")
# auth_token = os.getenv("AUTH_TOKEN")

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":os.getenv("ALPHAVANTAGE_API_KEY")
}

parameteres_news = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "from": "2025-10-16",
    "q":"Tesla",
    "sortBy":"popularity",
}

response_stock = requests.get("https://www.alphavantage.co/query", params=parameters_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()

response_news = requests.get("https://newsapi.org/v2/top-headlines", params=parameteres_news)
response_news.raise_for_status()
news = response_news.json()


current_date = dt.datetime.now()
date_yesterday = f"{current_date.year}-{current_date.month}-{current_date.day - 1 :02d}"
date_before_yesterday = f"{current_date.year}-{current_date.month}-{current_date.day - 2 :02d}"


company_close_yesterday = float(data_stock["Time Series (Daily)"][date_yesterday]["1. open"])
company_close_before_yesterday = float(data_stock["Time Series (Daily)"][date_before_yesterday]["4. close"])

company_percent_change = ((company_close_before_yesterday - company_close_yesterday) / company_close_yesterday) * 100

if company_percent_change >= 2 or company_percent_change <= -2:
    send_sms()
else:
    print(f"Change is {company_percent_change:.2f}%, not enough.")





