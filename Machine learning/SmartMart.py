#!/usr/bin/env python
# coding: utf-8

# In[328]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from holoviews.ipython import display
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error

groceries_DataFrame = pd.read_csv("inventory1.csv", nrows=3754)
groceries_DataFrame = groceries_DataFrame.fillna(0)


display(groceries_DataFrame)


# In[329]:


y = groceries_DataFrame['Restock']
y


# In[330]:


X = groceries_DataFrame.drop('Restock', axis=1)
X = X.drop('ProductName',axis=1)
X


# In[331]:



X_train, X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2, random_state = 100)


# In[332]:


X_train


# In[333]:


y_train


# In[334]:


X_test


# In[335]:


y_test


# In[336]:


lr = LinearRegression()
lr.fit(X_train,y_train)


# In[337]:


lr.score(X_test,y_test)


# In[338]:


y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)


# In[339]:


y_lr_train_pred


# In[340]:


print("This:", y_lr_test_pred)


# In[341]:



lr_train_mse = mean_squared_error(y_train,y_lr_train_pred)
lr_train_r2 = r2_score(y_train,y_lr_train_pred)
lr_train_mae = mean_absolute_error(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test,y_lr_test_pred)
lr_test_r2 = r2_score(y_test,y_lr_test_pred)
lr_test_mae = mean_absolute_error(y_test, y_lr_test_pred)


# In[342]:


lr_train_mse


# In[343]:


lr_train_r2 


# In[344]:


lr_train_mae


# In[345]:


lr_test_mse


# In[346]:


lr_test_r2


# In[347]:


lr_test_mae


# In[348]:


print('LR MSE (Train): ', lr_train_mse)
print('LR R2 (Train): ', lr_train_r2)
print('LR MSE (Test): ', lr_test_mse)
print('LR R2 (Test): ', lr_test_r2)


# In[349]:


lr_results = pd.DataFrame(['Linear regression', lr_train_mse,lr_train_r2,lr_train_mae,lr_test_mse,lr_test_r2,lr_test_mae]).transpose()
lr_results.columns = ['Method','Training MSE','Training R2','Training MAE','Testing MSE', 'Testing R2','Testing MAE']


# In[350]:


lr_results


# In[351]:



rf = RandomForestRegressor(max_depth = 2, random_state = 100)
rf.fit(X_train, y_train)
rf.score(X_test,y_test)


# In[352]:


y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)


# In[353]:


from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
rf_train_mse = mean_squared_error(y_train,y_rf_train_pred)
rf_train_r2 = r2_score(y_train,y_rf_train_pred)
rf_train_mae = mean_absolute_error(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test,y_rf_test_pred)
rf_test_r2 = r2_score(y_test,y_rf_test_pred)
rf_test_mae = mean_absolute_error(y_test, y_rf_test_pred)


# In[354]:


rf_results = pd.DataFrame(['Random Forest', rf_train_mse, rf_train_r2,rf_train_mae,rf_test_mse,rf_test_r2,rf_test_mae]).transpose()
rf_results.columns = ['Method','Training MSE','Training R2','Training MAE','Testing MSE','Testing MAE', 'Testing R2']
rf_results


# In[355]:


df_models = pd.concat([lr_results, rf_results], axis =0)
df_models

print(df_models)

# In[356]:


df_models.reset_index(drop = True)


# In[357]:



plt.scatter(x=y_test, y=y_lr_test_pred)

z = np.polyfit(y_test,y_lr_test_pred, 1)
p = np.poly1d(z)

plt.ylabel('Predict Logs')
plt.xlabel('Experimental Logs')

plt.plot


# In[358]:


plt.scatter(x=y_test, y=y_rf_test_pred)

z = np.polyfit(y_test,y_rf_test_pred, 1)
p = np.poly1d(z)

plt.ylabel('Predict Logs')
plt.xlabel('Experimental Logs')

