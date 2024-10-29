import requests
import sys

def get_stock():
    API_KEY = None
    # with open("API_KEY.txt") as file:
    #     API_KEY = file.read()
    if API_KEY == None:
        API_KEY = input("Enter your API key: ")

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    symbol = input("Enter symbol(IBM, APPL): ").lower()
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    # Find the first key and stock prices
    tmp = []
    first_key = list(data["Time Series (5min)"])[0]
    stock_prices = list(data["Time Series (5min)"][first_key].values())[:-1]

    # Update stock_prices list
    for price in stock_prices:
        tmp.append(float(price))
    stock_prices.clear()
    stock_prices = tmp.copy()

    price = sum(stock_prices) / len(stock_prices)

    print(f"{symbol}: {price:.2f}")
    while (1):
        exit = input("Press (E) to exit: ").lower()
        if exit == 'e':
            sys.exit(0)
        else:
            continue

# try:
#     cur_data = data["Time Series (5min)"]["2024-10-25 19:55:00"]
# except KeyError:
#     print("Sorry we out of rate limit per day. TT")
#     while (1):
#         exit = input("Press (E) to exit: ").lower()
#         if exit == 'e':
#             sys.exit(0)
#         else:
#             continue
        

# price = (float(cur_data['1. open']) + float(cur_data['4. close'])) / 2
# print(f"Price: {price}")
# while (1):
#     exit = input("Press (E) to exit: ").lower()
#     if exit == 'e':
#         sys.exit(0)
#     else:
#         continue
# print(API_KEY)
# print(data)
try:
    get_stock()
except KeyError:
    print("Sorry we out of rate limit per day. TT")
    while (1):
        exit = input("Press (E) to exit: ").lower()
        if exit == 'e':
            sys.exit(0)
        else:
            continue