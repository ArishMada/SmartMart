#Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', 10)

data=pd.read_csv("inventory1.csv")
print(data.head())

print(data.describe())

# Calculate the first and third quartiles
Q1 = data['Sales'].quantile(0.25)
Q3 = data['Sales'].quantile(0.75)

# IQR (Interquartile Range)
IQR = Q3 - Q1

# upper and lower bounds to identify outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the DataFrame to exclude rows with values outside the bounds
filtered_data = data[(data['Sales'] >= lower_bound) & (data['Sales'] <= upper_bound)]

new_data = filtered_data.iloc[:, 1:]

print(new_data)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(new_data)

print(pd.DataFrame(data_scaled).describe())

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

inertia_values = []
for k in range(1, 20):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow Method
plt.plot(range(1, 20), inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
# plt.show()

np.random.seed(5)

kmeans = KMeans(n_clusters = 2, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)

frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
print(frame['cluster'].value_counts())

rows_in_desired_cluster = frame[frame['cluster'] == 0].iloc[:, :-1]
print(rows_in_desired_cluster)

print(new_data.loc[3098])