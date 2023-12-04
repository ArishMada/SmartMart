#Import module
import pandas as pd

#Read csv
df = pd.read_csv("Sales Transaction.csv", encoding = "windows-1252")
print(df)

print(df.info())

# Count the negative values in the quantity column
count_negative_values = (df['Quantity'] < 0).sum()

print("Number of negative values in column:")
print(count_negative_values)

df['Quantity'] = df['Quantity'].apply(lambda x: abs(x) if x < 0 else x)

#Export result to csv
df.to_csv('Sales Transactions 1.csv', index=False)
