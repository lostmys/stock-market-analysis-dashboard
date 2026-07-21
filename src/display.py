def display_stock(quote):

    symbol = quote["01. symbol"]
    open_price = float(quote["02. open"])
    high_price = float(quote["03. high"])
    low_price = float(quote["04. low"])
    price = float(quote["05. price"])
    volume = int(quote["06. volume"])

    print("=" * 40)
    print("      STOCK INFORMATION")
    print("=" * 40)
    print(f"Symbol       :  {symbol}")
    print(f"Open         : {open_price: .2f}")
    print(f"Today's High : {high_price: .2f}")
    print(f"Today's Low  : {low_price: .2f}")
    print(f"Price        : {price: .2f}")
    print(f"Volume       : {volume: ,}")