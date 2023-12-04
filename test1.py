import pandas as pd

pd.set_option('display.max_columns', 10)
# Assuming your DataFrame is named 'your_dataframe'
df = pd.read_csv('inven.csv')

count_above_1 = df.isna().sum()

print("value count", count_above_1)

print(df.describe())

