Stock Portfolio Tracker:

CodeAlpha Python Programming Internship — Task 2:

A console-based stock portfolio calculator that allows users to build a personalized portfolio, calculate investment values, and export results to TXT or CSV files. Built using only Python's standard library.

Overview:
This application demonstrates fundamental Python programming concepts through a practical financial tool. Users can select from 10 predefined stocks, enter quantities, view a formatted portfolio summary, and export their data.

Note:All stock prices are manually defined sample values, not real-time market data.

Features:
✅ 10 predefined stocks with sample prices
✅ Input validation for symbols and quantities
✅ Multiple stock portfolio support
✅ Investment calculations with formatted summary
✅ Export to TXT or CSV format
✅ Error handling for file operations
✅ Standard library only (no external dependencies)

Available Stocks
-----------------------------------
| Symbol | Price | Symbol | Price |
| ------ | ----- | ------ | ----- |
| AAPL   | $180  | NVDA   | $120  |
| TSLA   | $250  | META   | $500  |
| GOOGL  | $140  | NFLX   | $680  |
| MSFT   | $420  | IBM    | $190  |
| AMZN   | $185  | ORCL   | $170  |
-----------------------------------

How It Works:
1.Display welcome message and available stocks
2.Input stock symbol (validated against available stocks)
3.Input quantity (validated as positive integer)
4.Calculate investment value (price × quantity)
5.Repeat for additional stocks (optional)
6.Display portfolio summary with totals
7.Export to TXT or CSV (optional)
8.Exit with goodbye message

Input Validation:

---------------------------------------------------------------------
| Input          | Validation                                       |
| -------------- | ------------------------------------------------ |
| Stock Symbol   | Cannot be empty; must exist in stock list        |
| Quantity       | Must be a positive whole number                  |
| Yes/No Prompts | Accepts "yes", "y", "no", "n" (case-insensitive) |
| File Format    | Must be "txt" or "csv"                           |
---------------------------------------------------------------------


Investment Calculation:
Investment Value = Price per Share × Quantity
Total Investment = Σ (Investment Value for each stock)

Technologies Used:

------------------------------------------------------
| Component             | Technology                 |
| --------------------- | -------------------------- |
| Language              | Python 3.x                 |
| Modules               | csv, os (standard library) |
| External Dependencies | None                       |
| GUI/API/Database      | Not used                   |
------------------------------------------------------


Program Structure:
------------------------------------------------------------------------
| Function                    | Purpose                                |
| --------------------------- | -------------------------------------- |
| display_welcome()           | Show welcome message and disclaimer    |
| display_available_stocks()  | List available stocks with prices      |
| get_stock_symbol()          | Get and validate stock symbol          |
| get_quantity()              | Get and validate quantity              |
| calculate_investment()      | Compute investment value               |
| ask_add_another()           | Prompt for additional stocks           |
| build_portfolio()           | Collect portfolio entries              |
| display_portfolio_summary() | Show formatted summary with totals     |
| save_as_txt()               | Export to TXT file                     |
| save_as_csv()               | Export to CSV file                     |
| save_portfolio()            | Handle file saving with error handling |
| main()                      | Program entry point                    |
------------------------------------------------------------------------
Example Execution:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
===================================================
           Stock Portfolio Tracker
  CodeAlpha Python Programming Internship - Task 2
===================================================

Available Stocks:
---------------------------
|Symbol    | Sample Price |
|AAPL      | $180.00      |
|TSLA      | $250.00      |
|GOOGL     | $140.00      |
|MSFT      | $420.00      |
|AMZN      | $185.00      |
|NVDA      | $120.00      |
|META      | $500.00      |
|NFLX      | $680.00      |
|IBM       | $190.00      |
|ORCL      | $170.00      |
---------------------------

Enter stock symbol: AAPL
Enter quantity: 10
Added: 10 share(s) of AAPL at $180.00 each.

Add another stock? (yes/no): yes

Enter stock symbol: TSLA
Enter quantity: 5
Added: 5 share(s) of TSLA at $250.00 each.

Add another stock? (yes/no): no

Portfolio Summary:

--------------------------------------------------------
Stock     Quantity     Price/Share     Investment Value
AAPL      10           $180.00         $1,800.00
TSLA      5            $250.00         $1,250.00
--------------------------------------------------------
TOTAL     15                           $3,050.00
--------------------------------------------------------


Save portfolio to a file? (yes/no): yes
Save as (txt/csv): csv

Portfolio saved successfully as 'portfolio_result.csv'.

Thank you for using Stock Portfolio Tracker. Goodbye!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Output Files:

portfolio_result.txt
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
STOCK PORTFOLIO SUMMARY
=============================================
(Sample stock prices - not live market data)

Symbol: AAPL, Quantity: 10, Price: $180.00, Investment: $1,800.00
Symbol: TSLA, Quantity: 5, Price: $250.00, Investment: $1,250.00

---------------------------------------------
Total Investment Value: $3,050.00
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
portfolio_result.csv
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Stock,Quantity,Price/Share,Investment Value
AAPL,10,180.00,1800.00
TSLA,5,250.00,1250.00

Total Investment Value,,,3050.00
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation & Usage:

Prerequisites:
Python 3.x
No external packages required

Running the Program:
# Clone repository
git clone <repository-url>
cd stock-portfolio-tracker
# Run the program
python stock_portfolio_tracker.py


Platform Commands:

----------------------------------------------------
| OS          | Command                            |
| ----------- | ---------------------------------- |
| Windows     | python stock_portfolio_tracker.py  |
| macOS/Linux | python3 stock_portfolio_tracker.py |
----------------------------------------------------


Project Structure:
stock-portfolio-tracker/
├── stock_portfolio_tracker.py    # Main script
├── portfolio_result.txt          # Generated TXT output
├── portfolio_result.csv          # Generated CSV output
└── README.md                     # Documentation

Limitations:
1]Static, hardcoded stock prices (not real-time)
2]No API or database connectivity
3]Console-based interface only
4]No portfolio editing after entry
5]No data persistence between sessions

Future Enhancements:
1]Real-time stock prices via API integration
2]Portfolio editing and deletion
3]Data persistence (file/database)
4]GUI interface (Tkinter/PyQt)
5]Additional export formats (JSON, Excel)
6]Portfolio analytics and charts

Internship Details:
-----------------------------------------------------
| Field   | Information                             |
| ------- | --------------------------------------- |
| Program | CodeAlpha Python Programming Internship |
| Task    | Task 2                                  |
| Project | Stock Portfolio Tracker                 |
| Type    | Console-based Python Application        |
-----------------------------------------------------

Author:-
Python Programming Intern:
CodeAlpha Internship Program

License:-
Educational project created for CodeAlpha Python Programming Internship.

Acknowledgments:-
1]CodeAlpha for the internship opportunity
2]Python community for documentation and resources
