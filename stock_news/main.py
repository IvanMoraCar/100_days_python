from datetime import datetime, timedelta
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_KEY = "LLONMPMGROIERMN3"
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_KEY = "dbc34056044d4145a0f1d687c1c05b73"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
account_sid = 'ACb13919c58c79d8b15ea87e85c58a44d3'
auth_token = '19d92c7755152e36b6ffc90e3043b64d'

TODAY = datetime.now()
YESTERDAY = TODAY - timedelta(days=1)
DAY_BEFORE_YESTERDAY = TODAY - timedelta(days=2)

formatted_yesterday = YESTERDAY.strftime('%Y-%m-%d')
formatted_day_before_yesterday = DAY_BEFORE_YESTERDAY.strftime('%Y-%m-%d')

# STEP 1: Check stock price changes
alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY
}

stock_response = requests.get(ALPHAVANTAGE_ENDPOINT, params=alphavantage_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Obtener los precios de cierre
stock_yesterday = float(stock_data["Time Series (Daily)"][formatted_yesterday]['4. close'])
stock_day_before_yesterday = float(stock_data["Time Series (Daily)"][formatted_day_before_yesterday]['4. close'])

# Calcular el porcentaje de cambio
percentage = abs(stock_yesterday - stock_day_before_yesterday) / stock_day_before_yesterday * 100
trend = "🔺" if stock_yesterday > stock_day_before_yesterday else "🔻"  # Indicador de subida o bajada

# Guardar el resultado del porcentaje
stock_info = f"TSLA: {trend}{percentage:.2f}%\n"

# STEP 2: Fetch news if the stock change is significant
if percentage >= 5:
    stock_info += "Fetching news about Tesla...\n"
    newsapi_params = {
        "q": COMPANY_NAME,
        "from": formatted_yesterday,
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY
    }

    newsapi_response = requests.get(NEWSAPI_ENDPOINT, params=newsapi_params)
    newsapi_response.raise_for_status()
    newsapi_data = newsapi_response.json()

    if "articles" in newsapi_data and newsapi_data["totalResults"] > 0:
        stock_info += "Last 3 news about Tesla:\n"
        for article in newsapi_data["articles"][:3]:  # Obtener las primeras 3 noticias
            stock_info += f"TSLA: {trend}{percentage:.2f}%\n"
            stock_info += f"Headline: {article['title']}\n"
            stock_info += f"Brief: {article['description']}\n"
            stock_info += f"URL: {article['url']}\n\n"
    else:
        stock_info += "No recent news found for Tesla.\n"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+17752626385',
        body=stock_info,
        to='+526632002998'
    )
