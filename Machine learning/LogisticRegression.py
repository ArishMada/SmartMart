import pandas as pd
import sklearn as sks
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('../Datasets/inventory1.csv')

X = df.drop(columns=['ProductName', 'Restock'], axis=1)
Y = df['Restock']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, Y_train)

LogisticRegression(max_iter=10000)

predictions = model.predict(X_test)

accuracy = accuracy_score(Y_test, predictions)
print('Accuracy: ', accuracy)

