# TransactionNo > 3
# Sales > 40
# Inventory < ROP

import pandas as pd

df = pd.read_csv('inventory1.csv')


# Define a function to apply based on conditions
def create_new_column(row):
    if (row['TransactionNo'] > 3 and row['Sales'] > 40) and (row['Inventory'] < row['ROP']):
        return 1
    else:
        return 0

df1 = pd.DataFrame()

df1["ProductName"] = df["ProductName"]

df1['Restock'] = df.apply(create_new_column, axis=1)

count_above_1 = (df1['Restock'] == 1).sum()

print("value count", count_above_1)

df1.to_csv('label.csv', index=False)


merged_df = pd.merge(df, df1, on='ProductName', how='left')

print(merged_df)

merged_df.to_csv('inventory1.csv', index=False)

# for index, row in df1.iterrows():
#     restock = row["Restock"]
#     pn = row["ProductName"]
#     if restock == 1:
#         print(pn)
#
# print(df[df['ProductName'] == '36 Foil Heart Cake Cases'][['TransactionNo', 'Sales', 'ROP', "Inventory"]])



