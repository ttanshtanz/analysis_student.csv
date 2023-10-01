#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[3]:


#input data
data = pd.read_csv("student.csv")
data.head(5)


# In[4]:


data.info()


# In[40]:


#total number of rows and columns
data.shape


# In[7]:


data.describe()


# In[8]:


data['math score'].head(5)


# In[10]:


#new cols - total score & percentage
data['Total score'] = data['math score']+data['reading score']+data['writing score']
data['Percentage'] = (data['Total score']/3).round(2)


# In[11]:


data.head(5)


# In[12]:


#check for missing values - all 0 means no Null values; else, that many rows has Null values
print(data.isna().sum())


# In[13]:


#taking count
data['gender'].value_counts()


# In[14]:


data['race/ethnicity'].value_counts()


# In[17]:


data['parental level of education'].value_counts()


# In[18]:


data['lunch'].value_counts()


# In[19]:


data['test preparation course'].value_counts()


# In[20]:


##Analysis
# gender                         - No of females is greater than males
# race/ethnicity                 - Majority of people are from Group C whereas A has the least 
# parental level of education    - Only 59 parents have masters degree where Most of the others have educated from some college.
# lunch                          - 2/3rd of the people takes lunch at standard rates.
# test preparation course        - Only 1/3rd of students took the taken preparation course. The rest haven't.


# In[22]:


#separating dataset as male and female
male = data[data['gender']=='male']
female = data[data['gender']=='female']


# In[23]:


male.head(5)


# In[24]:


female.head(5)


# In[33]:


#printing scores by using sum
print(f"{'*'*5} Math Scores {'*'*5}")
print(f"Males: ", round(male['math score'].sum()/len(male),3))
print("Females: {:.3f}".format(female['math score'].sum()/len(female)))


# In[34]:


print(f"{'*'*5} Reading Scores {'*'*5}")
print(f"Males: ", round(male['reading score'].sum()/len(male),3))
print("Females: {:.3f}".format(female['reading score'].sum()/len(female)))


# In[35]:


print(f"{'*'*5} Writing Scores {'*'*5}")
print(f"Males: ", round(male['writing score'].sum()/len(male),3))
print("Females: {:.3f}".format(female['writing score'].sum()/len(female)))


# In[39]:


#using mean function
mean_score = round(data.groupby('gender')['math score'].mean(),3)
mean_score


# In[42]:


#finding top performance - method 1 using nlargest
top_score = data['Total score'].nlargest(5)
top_score


# In[43]:


#finding top performance - method 2 by sorting
print(data.sort_values(['Total score'], ascending = False).head(5))


# In[50]:


data.info()


# In[59]:


#finding top performance - method 3 by merging & sorting using Pandas
top_score = pd.DataFrame(data['math score'] + data['reading score'] + data['writing score'], columns = ['Total Score'])

# Merge the 'top_score' DataFrame with the original DataFrame
merged_data = pd.merge(data, top_score, left_index=True, right_index=True)

# Sort the merged DataFrame by 'Total score' in descending order
sorted_data = merged_data.sort_values(by=['Total Score'], ascending=False)

# Display the sorted DataFrame
sorted_data


# ### Seaborn

# In[78]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt


# In[79]:


sns.set(style="whitegrid") #or darkgrid as bg


# In[80]:


# 1*2 subplots
fi, axs = plt.subplots(1, 2, figsize=(10,5))
sns.countplot(x='gender', data=data, ax=axs[0])
sns.countplot(x='race/ethnicity', data=data, ax=axs[1])


# In[81]:


# 2*2 subplots
fi, axs = plt.subplots(2, 2, figsize=(10,10))
sns.countplot(x='gender', data=data, ax=axs[0,0])
sns.countplot(x='race/ethnicity', data=data, ax=axs[0,1])
sns.countplot(x='parental level of education', data=data, ax=axs[1,0])
sns.countplot(x='test preparation course', data=data, ax=axs[1,1])


# In[88]:


# 3*3 subplots
fi, axs = plt.subplots(3, 3, figsize=(18,10))
sns.countplot(x='gender', data=data, ax=axs[0,0])
sns.countplot(x='race/ethnicity', data=data, ax=axs[0,1], order=data['race/ethnicity'].value_counts().index)
sns.countplot(x='parental level of education', data=data, ax=axs[0,2])
sns.countplot(x='lunch', data=data, ax=axs[1,0])
sns.countplot(x='test preparation course', data=data, ax=axs[1,1])
#cant use bar charts for 
sns.histplot(data['math score'], ax=axs[1, 2], bins=20)
sns.histplot(data['reading score'], ax=axs[2, 0], bins=20)
sns.histplot(data['writing score'], ax=axs[2, 1])
sns.histplot(data['Total score'], ax=axs[2, 2])

# Adjust the layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()


# In[ ]:




