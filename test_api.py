from api import get_current_price

stock = "AAPL"  # Apple stock
price = get_current_price(stock)

if price:
    print(f"✅ Current price of {stock} is ${price}")
else:
    print("❌ Failed to fetch price. Check your API key or stock symbol.")
