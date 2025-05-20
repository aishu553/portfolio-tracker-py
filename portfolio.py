import json
import os
from api import get_current_price

class Portfolio:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.stocks = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.stocks, f, indent=4)

    def add_stock(self, ticker, quantity, buy_price):
        self.stocks[ticker] = {
            "quantity": quantity,
            "buy_price": buy_price
        }
        self.save_data()
        print(f"{ticker} added to portfolio.")

    def remove_stock(self, ticker):
        if ticker in self.stocks:
            del self.stocks[ticker]
            self.save_data()
            print(f"{ticker} removed from portfolio.")
        else:
            print(f"{ticker} not found in portfolio.")

    def view_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
            return

        print("\nYour Portfolio:")
        print("{:<10} {:<10} {:<12} {:<15} {:<10}".format("Ticker", "Qty", "Buy Price", "Current Price", "P/L"))

        for ticker, info in self.stocks.items():
            quantity = info["quantity"]
            buy_price = info["buy_price"]
            current_price = get_current_price(ticker)

            if current_price is None:
                print(f"{ticker:<10} Data not available")
                continue

            profit = (current_price - buy_price) * quantity
            print(f"{ticker:<10} {quantity:<10} {buy_price:<12.2f} {current_price:<15.2f} {profit:<10.2f}")
