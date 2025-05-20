from portfolio import Portfolio

def menu():
    print("\n--- Stock Portfolio Tracker ---")
    print("1. View Portfolio")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. Exit")
    return input("Enter your choice: ")

def main():
    portfolio = Portfolio()

    while True:
        choice = menu()
        if choice == '1':
            portfolio.view_portfolio()
        elif choice == '2':
            ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter buy price: "))
            portfolio.add_stock(ticker, quantity, buy_price)
        elif choice == '3':
            ticker = input("Enter stock ticker to remove: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
