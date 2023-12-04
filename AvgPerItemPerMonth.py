#Import Module
import pandas as pd

#Read csv
df = pd.read_csv("Sales Transactions 1.csv", encoding = "windows-1252")
print(df)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year from the 'Date' column
df['MonthYear'] = df['Date'].dt.to_period('M')

# Calculate the average quantity sold per item per month
average_quantity_per_month = df.groupby(['ProductName', 'MonthYear'])['Quantity'].mean().reset_index()

# Round the average quantity to three decimal points
average_quantity_per_month['Quantity'] = average_quantity_per_month['Quantity']

print(average_quantity_per_month)

pivot_df = average_quantity_per_month.pivot(index='ProductName', columns='MonthYear', values='Quantity').reset_index().round(3)

# Rename the columns with the name of the month
month_names = pivot_df.columns[1:]  # Extract all columns starting from the second column
pivot_df.columns = ['ProductName'] + [f"{month.strftime('%B')}" if month.month != 12 else f"{month.strftime('%B')}_{month.year}" for month in month_names]

print(pivot_df)

#Change NaN data to 0
pivot_df = pivot_df.fillna(0)

print(pivot_df)

# Export the result to csv
pivot_df.to_csv('AverageQuantityPerMonthPerItem.csv', index=False)
