# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("inventory1.csv")

print(df)

y = df['Restock']
X = df.drop(columns=['ProductName', 'Restock'], axis=1)

print(X)

X_train, X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 100)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

result = pd.concat([df.loc[X_test.index, 'ProductName'], X_test], axis=1)

result = pd.DataFrame({'ProductName': result['ProductName'], 'Restock': y_pred})

result = result[result['Restock'].astype(str).str.contains('1', case=False)]

print(result['ProductName'])

