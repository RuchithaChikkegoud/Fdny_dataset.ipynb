#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#Import the Fire Department of New York City(FDNY) file
Fdny=pd.read_csv("C:/Users/dell/Downloads/14.FDNY.csv")
Fdny


# In[5]:


#View the content of the data
Fdny.info()


# In[6]:


#View the first five records
Fdny.head()


# In[7]:


#skip the duplicate header row
Fdny=Fdny.drop([0])
Fdny


# In[8]:


#Verify if the dataset is fixed
Fdny.info()


# In[9]:


#View the data statistics
Fdny.describe()


# In[10]:


#View the attributes of the dataset
Fdny.columns


# In[11]:


#View the index of the dataset
Fdny.index


# In[12]:


#count number of records for each attribute
Fdny.count()
#or
attribute_counts = Fdny.count()
print(attribute_counts)


# In[14]:


#View the datatypes of all three attributes
Fdny.dtypes
#or
datatype=Fdny.dtypes
print(datatype)


# In[15]:


#select FDNY information boroughwise
Fdny['Borough'].value_counts()


# In[16]:


Fdny.groupby('Borough')


# In[18]:


#select FDNY information for Manhattan
Fdny[Fdny['Borough']=='Manhattan']


# In[ ]:




