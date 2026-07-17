# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 350,
    "AMZN": 170
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Number of different stocks
n = int(input("Enter the number of different stocks: "))

# Input stock details
for i in range(n):
    stock = input("\nEnter Stock Name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Price per Share :", stock_prices[stock])
        print("Investment Value:", investment)
    else:
        print("Stock not found!")

# Display total investment
print("\n==============================")
print("Total Investment Value =", total_investment)
print("==============================")