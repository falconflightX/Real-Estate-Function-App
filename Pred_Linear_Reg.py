#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
from sklearn import linear_model


# In[23]:


df = pd.read_csv("C:/Users/l7927301/Downloads/Realestate.csv",sep=',')


# In[24]:


df=df.rename(columns={'X1 transaction date': "Date",'X2 house age':"Age",'X3 distance to the nearest MRT station':"Dist",'X4 number of convenience stores':"Num_stores",'X5 latitude':"Lat",'X6 longitude':"Long",'Y house price of unit area':"Price"})


# In[25]:


cols=['No','Date']
df=df.drop(cols, axis=1)


# In[26]:


df.head()


# In[28]:


x=df[['Age','Dist','Num_stores','Lat','Long']]
y=df[['Price']]


# In[29]:


reg = linear_model.LinearRegression()
reg.fit(x,y)


# In[30]:


print(reg.score(x,y))
print(reg.predict([[25,251,5,24.9756,121.5521]]))
print(reg.coef_)
print(reg.intercept_)


# In[31]:


#from sklearn.externals import joblib
import joblib
joblib.dump(reg,"linear_reg.pkl")


# In[ ]:




