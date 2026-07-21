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
 return quote
 