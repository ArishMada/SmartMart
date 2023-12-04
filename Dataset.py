import numpy as np
import pandas as pd

df = pd.read_csv("inventory.csv", encoding = "windows-1252")
print(df)

additional_info = pd.read_csv('AverageQuantityPerMonthPerItem.csv')

additional_info1 = pd.read_csv('AverageQuantityPerItem2019.csv')

additional_info2 = pd.read_csv('AverageTransactionPerItem.csv')

# Merge the two DataFrames based on the 'ProductNo' column
merged_df = pd.merge(df, additional_info, on='ProductName', how='left')

merged_df1 = pd.merge(merged_df, additional_info1, on='ProductName', how='left')

merged_df2 = pd.merge(merged_df1, additional_info2, on='ProductName', how='left')

nan_count_per_column = merged_df1.isna().sum()

count_of_value = merged_df1['MeanValue'].value_counts().get(0, 0)

print(count_of_value)

merged_df2 = merged_df2.fillna(0)
print(merged_df1)

count_negative_values = (merged_df1['MeanValue'] < 0).sum()

print("Number of negative values in column:")
print(count_negative_values)

# Create the new column for SafetyStock
merged_df2['SafetyStock'] = np.ceil(merged_df2['MeanValue'])

# Create the new Column for Lead Time - 1month=1 and 0.03 = 1day
np.random.seed(42)
random_values = np.arange(0, 3.03, 0.03)
np.random.shuffle(random_values)

merged_df2['LeadTime'] = np.random.choice(random_values, size=len(merged_df2))

# Create the new column for the ROP = Demand during lead time + SafetyStock
merged_df2['ROP'] = merged_df2['LeadTime'] * merged_df2['MeanValue'] + merged_df2['SafetyStock']

print(merged_df2['ROP'])

# Create a new column Rating
merged_df2['Rating'] = np.random.normal(loc=4.2, scale=1.0, size=len(merged_df2))

merged_df2['Rating'] = merged_df2['Rating'].clip(0.0, 5.0)

print(merged_df1)

# median_value = merged_df1['Rating'].median()
# mean_value = merged_df1['Rating'].mean()
#
# print(f"The median of is: {median_value}")
# print(f"The mean of is: {mean_value}")
#
# count_above_3_5 = (merged_df1['Rating'] > 3.5).sum()
#
# print(count_above_3_5)


bio_column = np.random.choice([0, 1], size=len(merged_df1), p=[0.80, 0.20])
merged_df2['Bio'] = bio_column

count_above_1 = merged_df2.isna().sum()

print("value count", count_above_1)

print(merged_df2)
merged_df2.to_csv('inventory1.csv', index=False)