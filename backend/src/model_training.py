import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Connect to SQLite database
conn = sqlite3.connect('data/historical_data.db')

# Load the preprocessed training data from the SQL table
train_df = pd.read_sql_query("SELECT * FROM train_data", conn, index_col='Date', parse_dates=True)

# Close the connection
conn.close()

# Define features and target variable (assuming USD/BRL is the target)
X = train_df.drop(columns=['USD/BRL'])
y = train_df['USD/BRL']

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'models/currency_prediction_model.pkl')
