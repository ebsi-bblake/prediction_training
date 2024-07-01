import yfinance as yf
import pandas as pd
import sqlite3

# Define the tickers for BRICS currencies, gold, and oil
tickers = {
    'USD/BRL': 'BRL=X',
    'USD/RUB': 'RUB=X',
    'USD/INR': 'INR=X',
    'USD/CNY': 'CNY=X',
    'USD/ZAR': 'ZAR=X',
    'USD/XAU': 'GC=F',  # Gold futures
    'USD/OIL': 'CL=F'   # Crude oil futures
}

# Collect historical data for the last 10 years
start_date = '2010-01-01'
end_date = '2023-12-31'

# Download data
data = {}
for name, ticker in tickers.items():
    data[name] = yf.download(ticker, start=start_date, end=end_date)['Close']

# Combine data into a single DataFrame
df = pd.DataFrame(data)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('data/historical_data.db')

# Save the data to a SQL table
df.to_sql('historical_data', conn, if_exists='replace', index_label='Date')

# Close the connection
conn.close()
