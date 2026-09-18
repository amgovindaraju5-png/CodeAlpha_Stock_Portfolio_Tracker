"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship — Task 2

A simple console-based stock portfolio calculator. Stock prices are
manually defined (hardcoded) sample values, NOT live market prices.
Uses only Python's standard library.
"""

import csv
import os

# Manually defined sample stock prices (NOT live market data)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
    "NVDA": 120,
    "META": 500,
    "NFLX": 680,
    "IBM": 190,
    "ORCL": 170
}


def display_welcome():
    """Show a clean welcome message and explain the sample-data disclaimer."""
    print("=" * 46)
    print("           Stock Portfolio Tracker")
    print("  CodeAlpha Python Programming Internship - Task 2")
    print("=" * 46)
    print("\nNote: Stock prices below are manually defined")
    print("sample prices, not real-time market prices.\n")


def display_available_stocks(stock_prices):
    """Print available stock symbols and their sample prices in aligned columns."""
    print("Available Stocks\n")
    print(f"{'Symbol':<11}{'Sample Price'}")
    for symbol, price in stock_prices.items():
        print(f"{symbol:<11}${price:,.2f}")
    print()


def get_stock_symbol(stock_prices):
    """
    Ask the user for a stock symbol and validate that it exists
    in the STOCK_PRICES dictionary. Keeps asking until valid.
    """
    while True:
        symbol = input("Enter stock symbol: ").upper().strip()

        if len(symbol) == 0:
            print("Error: Stock symbol cannot be empty. Please try again.\n")
        elif symbol not in stock_prices:
            print(f"Error: '{symbol}' is not in the available stock list. Please try again.\n")
        else:
            return symbol


def get_quantity():
    """
    Ask the user for a quantity and validate that it is a positive
    whole number. Keeps asking until valid.
    """
    while True:
        quantity_input = input("Enter quantity: ").strip()

        if len(quantity_input) == 0:
            print("Error: Quantity cannot be empty. Please try again.\n")
            continue

        if not quantity_input.isdigit():
            print("Error: Quantity must be a positive whole number. Please try again.\n")
            continue

        quantity = int(quantity_input)

        if quantity <= 0:
            print("Error: Quantity must be greater than zero. Please try again.\n")
            continue

        return quantity


def calculate_investment(price, quantity):
    """Calculate the investment value for one stock entry."""
    return price * quantity


def ask_add_another():
    """Ask the user if they want to add another stock to the portfolio."""
    while True:
        choice = input("Add another stock? (yes/no): ").lower().strip()
        if choice in ("yes", "y"):
            print()
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Error: Please answer 'yes' or 'no'.\n")


def build_portfolio(stock_prices):
    """
    Collect one or more stock entries from the user.
    Returns a list of dictionaries, one per stock entry.
    """
    portfolio = []

    while True:
        symbol = get_stock_symbol(stock_prices)
        quantity = get_quantity()
        price = stock_prices[symbol]
        investment = calculate_investment(price, quantity)

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"Added: {quantity} share(s) of {symbol} at ${price:,.2f} each.\n")

        if not ask_add_another():
            break

    return portfolio


def display_portfolio_summary(portfolio):
    """Print a formatted summary of every stock entry and the grand total."""
    print("\nPortfolio Summary\n")
    print(f"{'Stock':<10}{'Quantity':<13}{'Price/Share':<16}{'Investment Value'}")

    total_quantity = 0
    total_investment = 0
    for entry in portfolio:
        total_quantity += entry["quantity"]
        total_investment += entry["investment"]
        price_str = f"${entry['price']:,.2f}"
        inv_str = f"${entry['investment']:,.2f}"
        print(f"{entry['symbol']:<10}{entry['quantity']:<13}{price_str:<16}{inv_str}")

    print("-" * 46)
    print()
    total_inv_str = f"${total_investment:,.2f}"
    print(f"{'TOTAL':<10}{total_quantity:<13}{'':<16}{total_inv_str}")

    return total_investment


def ask_save_choice():
    """Ask the user whether they want to save the portfolio to a file."""
    while True:
        choice = input("\nSave portfolio to a file? (yes/no): ").lower().strip()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Error: Please answer 'yes' or 'no'.")


def get_file_format_choice():
    """Ask the user whether to save as .txt or .csv."""
    while True:
        choice = input("Save as (txt/csv): ").lower().strip()
        if choice in ("txt", "csv"):
            return choice
        else:
            print("Error: Please enter 'txt' or 'csv'.")


def save_as_txt(portfolio, total_investment, filename):
    """Save the portfolio summary to a plain text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 45 + "\n")
        file.write("(Sample stock prices - not live market data)\n\n")

        for entry in portfolio:
            file.write(
                f"Symbol: {entry['symbol']}, "
                f"Quantity: {entry['quantity']}, "
                f"Price: ${entry['price']:,.2f}, "
                f"Investment: ${entry['investment']:,.2f}\n"
            )

        file.write("\n" + "-" * 45 + "\n")
        file.write(
            f"Total Investment Value: ${total_investment:,.2f}\n"
        )


def save_as_csv(portfolio, total_investment, filename):
    """Save the portfolio summary to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Quantity", "Price/Share", "Investment Value"])

        for entry in portfolio:
            writer.writerow([
                entry["symbol"],
                entry["quantity"],
                f"{entry['price']:.2f}",
                f"{entry['investment']:.2f}"
            ])

        writer.writerow([])
        writer.writerow([
            "Total Investment Value",
            "",
            "",
            f"{total_investment:.2f}"
        ])


def save_portfolio(portfolio, total_investment):
    """Save the portfolio as a TXT or CSV file in the project folder."""
    file_format = get_file_format_choice()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(
        script_dir,
        f"portfolio_result.{file_format}"
    )

    try:
        if file_format == "txt":
            save_as_txt(portfolio, total_investment, filename)
        else:
            save_as_csv(portfolio, total_investment, filename)

        if os.path.exists(filename):
            print(
                f"\nPortfolio saved successfully as "
                f"'portfolio_result.{file_format}'."
            )
        else:
            print("\nError: The file was not created.")

    except PermissionError:
        print("\nError: Permission denied. Please close the file if it is open.")

    except OSError as e:
        print(f"\nError: Could not save the file: {e}")


def main():
    """Program entry point: welcome, build portfolio, summarize, save."""
    display_welcome()
    display_available_stocks(STOCK_PRICES)

    portfolio = build_portfolio(STOCK_PRICES)
    total_investment = display_portfolio_summary(portfolio)

    if ask_save_choice():
        save_portfolio(portfolio, total_investment)

    print("\nThank you for using Stock Portfolio Tracker. Goodbye!")


if __name__ == "__main__":
    main()