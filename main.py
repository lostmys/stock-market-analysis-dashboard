from src.api import get_stock_data

symbol = input("Enter stock symbol: ").strip().upper()

stock = get_stock_data(symbol)

print(stock)