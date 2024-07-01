import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split

# Connect to SQLite database
conn = sqlite3.connect('data/historical_data.db')

# Load the collected data from the SQL table
df = pd.read_sql_query("SELECT * FROM historical_data", conn, index_col='Date', parse_dates=True)

# Close the connection
conn.close()

# Fill missing values using forward fill and backward fill
df.ffill(inplace=True)
df.bfill(inplace=True)

# Example normalization (scaling the data)
df_normalized = (df - df.mean()) / df.std()

# Split the data into training and testing sets
train_df, test_df = train_test_split(df_normalized, test_size=0.2, shuffle=False)

# Connect to SQLite database
conn = sqlite3.connect('data/historical_data.db')

# Save the preprocessed data to SQL tables
train_df.to_sql('train_data', conn, if_exists='replace', index_label='Date')
test_df.to_sql('test_data', conn, if_exists='replace', index_label='Date')

# Close the connection
conn.close()
