#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.metrics import f1_score
from utils import is_thursday
import tarfile


# In[2]:


with tarfile.open('test.tar.gz', 'r:gz') as tar:
    tar.extractall()


# In[3]:


df = pd.read_csv('test.psv', sep='|', header=1)


# In[4]:


thursdays = df[df.dates.apply(is_thursday)]


# In[5]:


y_true = thursdays['y'].values
y_pred = thursdays['yhat'].values
f1_score_of_thursdays = f1_score(y_true, y_pred)


# In[6]:


print('f1 for Thursdays: {:.3f}'.format(f1_score_of_thursdays))


# In[ ]:




