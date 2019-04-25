#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


data = pd.read_csv('data.csv')


# In[ ]:





# In[32]:


datainput = {
    0: "1",
    1: "P",
    2: "5",
    3: "a",
    4: "A"
}


# In[33]:


for i in range(89):
    s = 0
    for j in range(5):
        if data.iloc[i,j] == datainput[j]:
            s = s+1
    data.loc[i,'Score'] = s


# In[34]:


df = data.sort_values(by=['Score'],ascending=False)


# In[31]:


recommedation = df.head(5)


# In[ ]:




