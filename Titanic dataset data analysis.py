#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pandas')


# In[2]:


import pandas as pd


# In[4]:


data = {
    "id":[1,2,3,4,5],
    "name":["Ikra", "Sohana", "Setu", "Shakib", "Tanvir"],
    "Dept": ["CSE", "IT", "BBA", "MBA","Civil"],
}


# In[5]:


pd.DataFrame(data)


# In[6]:


#https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv


# In[7]:


# import data from csv?web
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[8]:


df


# In[9]:


#eda = exploretory data analysis
# data analysis
# feature engineering - data cleaning, pre-processing
# feature selection


# In[13]:


# row call
df.iloc[0]


# In[14]:


# row call
df.iloc[0:5]


# In[19]:


df.head(5)


# In[20]:


# cloumn call
df["Name"]


# In[23]:


# cloumn call
df["Name"].head(10)


# In[22]:


df["Name"].tail(5)


# In[25]:


df['Pclass'].head()


# In[26]:


df['Name'][10:15]


# In[28]:


df[['Name', "Pclass"]][10:15]


# In[29]:


# fetch cloumn name
df.columns


# In[31]:


df.dtypes


# In[33]:


#statistical description
df.describe()


# In[34]:


#total data
df.shape


# In[38]:


#finding null value
df.isna()


# In[39]:


df.isna().sum()


# In[40]:


# search a specific item
df[df["Name"]=="Braund, Mr. Owen Harris"]


# In[41]:


# search a specific item
df[["Name", "Age", "Pclass"]][df["Name"]=="Braund, Mr. Owen Harris"]


# In[47]:


df[["Name", "Age", "Pclass"]][df["Age"]<=30]


# In[48]:


df[["Name", "Age", "Pclass"]][df["Age"]<=30].count()


# In[51]:


df[["Name", "Age", "Pclass"]][(df["Age"]>=30) & (df["Age"]<=40)]


# In[52]:


sorted(df["Pclass"].unique())


# In[54]:


sorted(df["SibSp"].unique())


# In[55]:


df["Pclass"].value_counts()


# In[56]:


df["SibSp"].value_counts()


# In[57]:


df.head()


# In[58]:


#add column/rowa
df["Boat"] = "Nan"


# In[59]:


df.head()


# In[60]:


#delete column/row(If your want to delete permanently have to use inplace=True)
df.drop("Boat", axis=1, inplace=True)


# In[61]:


df.head()


# In[62]:


df["Embarked"]. unique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




