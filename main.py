import yfinance as yf

# Set the ticker symbol for the stock you are interested in
ticker = "AAPL"

# Get stock data from Yahoo Finance
stock_data = yf.Ticker(ticker).info

# Check the stock's price-to-earnings ratio (P/E ratio)
pe_ratio = stock_data['regularMarketPrice'] / stock_data['trailingEps']

# Check the stock's dividend yield
dividend_yield = stock_data['trailingAnnualDividendYield']

# Check the stock's earnings growth rate
earnings_growth_rate = stock_data['earningsGrowth']

# Set the threshold for the P/E ratio, dividend yield, and earnings growth rate
pe_ratio_threshold = 20
dividend_yield_threshold = 2.5
earnings_growth_rate_threshold = 10

# Determine if the stock is a good investment based on the criteria
if pe_ratio < pe_ratio_threshold and dividend_yield > dividend_yield_threshold and earnings_growth_rate > earnings_growth_rate_threshold:
  print(f"{ticker} is a good investment.")
else:
  print(f"{ticker} is not a good investment.")
