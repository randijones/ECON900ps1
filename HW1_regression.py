#!/usr/bin/env python
# coding: utf-8

# In[142]:


import numpy as np
import os
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
import statsmodels.api as sm
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn-whitegrid')


# In[119]:


df = pd.read_csv("historical_dataset.csv")


# In[120]:


print (df)


# In[121]:


df.head()


# In[122]:


df.info()


# In[123]:


df.sort_values(['date'], ascending = [True], inplace = True)
df.head()


# In[124]:


print (df.iloc[:,2])


# In[125]:


target = df.iloc[:,2].values
data = df.iloc[:,4:6]

print(data.head())


# In[126]:


regression = linear_model.LinearRegression()

regression.fit(data, target)

X = [
    [0,0],
    [10,10],
]

results = regression.predict(X)
print(results)


# In[127]:


N= 300
open_price=df.iloc[:,2]
day_low=df.iloc[:,4]
plt.scatter(day_low, open_price, color='g')
plt.xlabel('day_low')
plt.ylabel('open_price')
plt.show()


# In[128]:


N=300
open_price=df.iloc[:,2]
close_price=df.iloc[:,5]
plt.scatter(close_price, open_price, color='r')
plt.xlabel('close_price')
plt.ylabel('open_price')
plt.show()


# In[151]:


df['close']=df.iloc[:,5]
df['open']=df.iloc[:,2]


# In[148]:


df['close']=df.iloc[:,5]
print (df['close'])


# In[159]:


data=df['close']
target=df['open']
model=sm.OLS(target,data).fit()
predictions=model.predict(data)
model.summary()


# In[158]:


data=df['close']
target=df['open']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()


# In[160]:


df['close']= df.iloc[:,5]
df['day_high']=df.iloc[:,3]


# In[161]:


data=df['close']
target=df['day_high']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()


# In[163]:


df['close']= df.iloc[:,5]
df['day_low']=df.iloc[:,4]


# In[164]:


data=df['close']
target=df['day_low']
data = sm.add_constant(data)
model=sm.OLS(target, data).fit()
predictions=model.predict(data)
model.summary()


# In[ ]:





# In[ ]:




