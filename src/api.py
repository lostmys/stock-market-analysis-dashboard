import requests
api_key="W7GQWC66H0S40TMF"

def get_stock_data(symbol):

 url=(
    f"https://www.alphavantage.co/query"
    f"?function=GLOBAL_QUOTE"
    f"&symbol={symbol}"
    f"&apikey={api_key}"
 )
 response=requests.get(url)
 data=response.json()

 quote = data["Global Quote"]
 print(f"SYMBOL: {quote["01. symbol"]}")
 print(f"open: {quote["02. open"]}")
 print(f"high: {quote["03. high"]}")
 print(f"low: {quote["04. low"]}")
 print(f"price: {quote["05. price"]}")
 print(f"volume: {quote["06. volume"]}")
 