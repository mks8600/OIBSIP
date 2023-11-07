#!/usr/bin/env python
# coding: utf-8

# # Task 2 unemloyment rate 

#  Importing Necessary Libraries

# In[1]:


import numpy as np
import pandas as pd


# ## Reading CSV File

# In[2]:


df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape  #Returns tuple of shape (Rows,Columns) of dataframe


# In[6]:


df.info() #Prints info about dataframe


# In[7]:


df.describe() #Prints numerical decription of the data in dataframe


# In[8]:


x=df['Region']


# In[9]:


x


# In[10]:


y=df[' Estimated Unemployment Rate (%)']


# In[11]:


y


# In[12]:


df2=df.iloc[:,3]


# In[13]:


df2


# ## Importing Necessary Libraries

# In[14]:


import plotly.express as px
import matplotlib.pyplot as plt


# ## Analyzing Data by bar graphs

# In[15]:


fg=px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[16]:


fg=px.bar(df,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (Region-Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# # unemployment state wise  graph 

# In[17]:


fg=px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[18]:


fg=px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Scatter Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[19]:


fg=px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

