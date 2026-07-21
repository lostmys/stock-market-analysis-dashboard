import src 
from src.api import get_stock_data
from src.display import display_stock
symbol = input("Enter stock symbol: ").strip().upper()

stock = get_stock_data(symbol)

display_stock(stock) 