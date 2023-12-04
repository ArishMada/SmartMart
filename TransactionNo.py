#Import module
import pandas as pd

#Set pandas display max 10 columns
pd.set_option('display.max_columns', 10)

#Read csv
df = pd.read_csv('Sales Transactions 1.csv')

# Group by 'ProductNo' and count the number of transactions per item
transactions_per_item = df.groupby('ProductNo')['TransactionNo'].count().reset_index()

print(transactions_per_item)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Extract the year and month from the 'Date' column
df['YearMonth'] = df['Date'].dt.to_period('M')

# Group by 'ProductNo' and 'YearMonth', then count the number of transactions per month for each product
transactions_per_month_per_item = df.groupby(['ProductName', 'YearMonth'])['TransactionNo'].count().reset_index()

# Calculate the average number of transactions per month for each product
average_transactions_per_month = transactions_per_month_per_item.groupby('ProductName')['TransactionNo'].mean().reset_index().round(3)

print(average_transactions_per_month)

#Export result to csv
average_transactions_per_month.to_csv('AverageTransactionPerItem.csv', index=False)
