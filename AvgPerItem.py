#import modules
import pandas as pd

#Read csv
df = pd.read_csv("Datasets/AverageQuantityPerMonthPerItem.csv", encoding="windows-1252")
print(df)

#Create new column "MeanValue"
df['MeanValue'] = df[['December_2018', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December_2019']].mean(axis=1)

#Export ProductName and MeanValue to csv
average_quantity = df[['ProductName', 'MeanValue']].copy()
average_quantity.to_csv('Datasets/AverageQuantityPerItem.csv', index=False)

print(average_quantity)
