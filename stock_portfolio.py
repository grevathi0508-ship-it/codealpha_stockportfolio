# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("========================================")
print("       STOCK PORTFOLIO TRACKER")
print("========================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter the stocks you want to buy.")
print("Type 'done' when you are finished.")

while True:

    stock = input("\nEnter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add stock to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"{quantity} shares of {stock} added successfully!")

# Calculate total investment
total_value = 0

print("\n========================================")
print("             YOUR PORTFOLIO")
print("========================================")

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Value':<12}")
    print("-" * 44)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        total_value += value

        print(f"{stock:<10}{quantity:<10}${price:<11}${value:<11}")

    print("-" * 44)
    print(f"Total Investment: ${total_value}")

print("\nThank you for using Stock Portfolio Tracker!")