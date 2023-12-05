import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn import metrics

df = pd.read_csv('inventory1.csv')

df.drop('ProductName', axis=1, inplace=True)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

print(X_train)

print(y_train)

print(X_test)

print(y_test)

nbc = GaussianNB()

nbc.fit(X_train,y_train)

y_pred = nbc.predict(X_test)
mislabel = np.sum((y_test!=y_pred))
print("Total number of mislabelled data points from {} test samples is {}".format(len(y_test),mislabel))

print("The classification report is as follows...\n")
print(y_pred)

print("Accuracy: ",metrics.accuracy_score(y_test,y_pred))



