#!/usr/bin/env python
# coding: utf-8

# ### Name: Mai Dang Nhat Anh - ID: ITDSIU19031  
# 
# # MID-TERM EXAMINATION  
#   
# Given the glass identification data set, which can be found at http://archive.ics.uci.edu/ml/datasets/glass+identification, including the following attributes:  
# %    1. Id number: 1 to 214  
# %    2. RI: refractive index  
# %    3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as   
# %                   are attributes 4-10)  
# %    4. Mg: Magnesium  
# %    5. Al: Aluminum  
# %    6. Si: Silicon  
# %    7. K: Potassium  
# %    8. Ca: Calcium  
# %    9. Ba: Barium  
# %   10. Fe: Iron  
# %   11. Type of glass: (class attribute)  
# %       -- 1 building_windows_float_processed  
# %       -- 2 building_windows_non_float_processed  
# %       -- 3 vehicle_windows_float_processed  
# %       -- 4 vehicle_windows_non_float_processed (none in this database)  
# %       -- 5 containers  
# %       -- 6 tableware  
# %       -- 7 headlamps  
# Attributes from 2 to 10 are numeric.
# 
# 
# 

# ### Q1.(40pts) Select 20 sample records from the data set (file glass.data), draw boxplots for Attributes 2-10 using excel or R or Python. Note: please list the selected records and then present the boxplots.

# First, we import some libraries for the task

# In[2]:


import random
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Import the data and take sample of 20, put it in a dataframe

# In[3]:


data= pd.read_csv (r'C:\Users\asus\Downloads\Documents\IntrotoDS\Mai Dang Nhat Anh - ITDSIU19031\glass.data',header=None,usecols=[1,2,3,4,5,6,7,8,9])
#print(data)
sample = data.sample(20)
df = pd.DataFrame(sample)
df


# Sketch the boxplot of 9 variables from attribute 2 - 10

# In[14]:


fig, axes = plt.subplots(nrows=1, ncols=9, figsize=(20, 10))

df[1].plot.box(ax=axes[0])
df[2].plot.box(ax=axes[1])
df[3].plot.box(ax=axes[2])
df[4].plot.box(ax=axes[3])
df[5].plot.box(ax=axes[4])
df[6].plot.box(ax=axes[5])
df[7].plot.box(ax=axes[6])
df[8].plot.box(ax=axes[7])
df[9].plot.box(ax=axes[8])

axes[0].set_title('attr 2')
axes[1].set_title('attr 3')
axes[2].set_title('attr 4')
axes[3].set_title('attr 5')
axes[4].set_title('attr 6')
axes[5].set_title('attr 7')
axes[6].set_title('attr 8')
axes[7].set_title('attr 9')
axes[8].set_title('attr 10')

fig.tight_layout()
plt.show()


# ### Q2. (30pts) Compare and remark the five-number summaries from the above boxplots with the Summary Statistics of the corresponding attributes described in file glass.names.

# In[15]:


print("min:",min(df[1]))
print("Q1:",scipy.percentile(df[1],25))
print("Q2:",scipy.median(df[1]))
print("Q3",scipy.percentile(df[1],75))
print("max:",max(df[1]))


# In[16]:


print("min:",min(df[2]))
print("Q1:",scipy.percentile(df[2],25))
print("Q2:",scipy.median(df[2]))
print("Q3",scipy.percentile(df[2],75))
print("max:",max(df[2]))


# In[17]:


print("min:",min(df[3]))
print("Q1:",scipy.percentile(df[3],25))
print("Q2:",scipy.median(df[3]))
print("Q3",scipy.percentile(df[3],75))
print("max:",max(df[3]))


# In[18]:


print("min:",min(df[4]))
print("Q1:",scipy.percentile(df[4],25))
print("Q2:",scipy.median(df[4]))
print("Q3",scipy.percentile(df[4],75))
print("max:",max(df[4]))


# In[19]:


print("min:",min(df[5]))
print("Q1:",scipy.percentile(df[5],25))
print("Q2:",scipy.median(df[5]))
print("Q3",scipy.percentile(df[5],75))
print("max:",max(df[5]))


# In[20]:


print("min:",min(df[6]))
print("Q1:",scipy.percentile(df[6],25))
print("Q2:",scipy.median(df[6]))
print("Q3",scipy.percentile(df[6],75))
print("max:",max(df[6]))


# In[21]:


print("min:",min(df[7]))
print("Q1:",scipy.percentile(df[7],25))
print("Q2:",scipy.median(df[7]))
print("Q3",scipy.percentile(df[7],75))
print("max:",max(df[7]))


# In[22]:


print("min:",min(df[8]))
print("Q1:",scipy.percentile(df[8],25))
print("Q2:",scipy.median(df[8]))
print("Q3",scipy.percentile(df[8],75))
print("max:",max(df[8]))


# In[23]:


print("min:",min(df[9]))
print("Q1:",scipy.percentile(df[9],25))
print("Q2:",scipy.median(df[9]))
print("Q3",scipy.percentile(df[9],75))
print("max:",max(df[9]))


# Remark: The five-number summary that we calculated is similar to the Summary Statistic in the boxplot

# ### Q3. (30pts) Pick up one of the 20 sample records and find TWO nearest records using Euclidean and Manhattan distance metrics, using excel or R or Python. These comparisons are performed on the numeric attributes 2-10 only, exclude the type attribute. Note: please provide the selected records before listing the two nearest records, and explain how you get results.

# We choose a record from the sample we have taken in Q1

# In[33]:


sample1 = sample.sample(1)
selectRe = pd.DataFrame(sample1)
selectRe


# We see that is the 2nd row from the dataframe  
#   
# Then, we assign value for each row from dataframe

# In[34]:


row1 = df.iloc[0]
row1


# In[35]:


row2 = df.iloc[1]
row3 = df.iloc[2]
row4=df.iloc[3]
row5=df.iloc[4]
row6=df.iloc[5]
row7=df.iloc[6]
row8=df.iloc[7]
row9=df.iloc[8]
row10=df.iloc[9]
row11=df.iloc[10]
row12=df.iloc[11]
row13=df.iloc[12]
row14=df.iloc[13]
row15=df.iloc[14]
row16=df.iloc[15]
row17=df.iloc[16]
row18=df.iloc[17]
row19=df.iloc[18]
row20=df.iloc[19]


# Import distance from the library scipy for K-NN calculation

# In[36]:


from scipy.spatial import distance


# Calculate the Euclidean Distance of each row to the selected row

# In[37]:


dst1 = distance.euclidean(selectRe, row1)
dst2 = distance.euclidean(selectRe,row2)
dst3 = distance.euclidean(selectRe,row3)
dst4 = distance.euclidean(selectRe,row4)
dst5 = distance.euclidean(selectRe,row5)
dst6 = distance.euclidean(selectRe,row6)
dst7 = distance.euclidean(selectRe,row7)
dst8 = distance.euclidean(selectRe,row8)
dst9 = distance.euclidean(selectRe,row9)
dst10 = distance.euclidean(selectRe,row10)
dst11 = distance.euclidean(selectRe,row11)
dst12 = distance.euclidean(selectRe,row12)
dst13 = distance.euclidean(selectRe,row13)
dst14 = distance.euclidean(selectRe,row14)
dst15 = distance.euclidean(selectRe,row15)
dst16 = distance.euclidean(selectRe,row16)
dst17 = distance.euclidean(selectRe,row17)
dst18 = distance.euclidean(selectRe,row18)
dst19 = distance.euclidean(selectRe,row19)
dst20 = distance.euclidean(selectRe,row20)


# In[38]:


print("distance from the selected record to row1=",dst1)
print("distance from the selected record to row2=",dst2)
print("distance from the selected record to row3=",dst3)
print("distance from the selected record to row4=",dst4)
print("distance from the selected record to row5=",dst5)
print("distance from the selected record to row6=",dst6)
print("distance from the selected record to row7=",dst7)
print("distance from the selected record to row8=",dst8)
print("distance from the selected record to row9=",dst9)
print("distance from the selected record to row10=",dst10)
print("distance from the selected record to row11=",dst11)
print("distance from the selected record to row12=",dst12)
print("distance from the selected record to row13=",dst13)
print("distance from the selected record to row14=",dst14)
print("distance from the selected record to row15=",dst15)
print("distance from the selected record to row16=",dst16)
print("distance from the selected record to row17=",dst17)
print("distance from the selected record to row18=",dst18)
print("distance from the selected record to row19=",dst19)
print("distance from the selected record to row20=",dst20)


# In[39]:


euclidean=[dst1,dst2,dst3,dst4,dst5,dst6,dst7,dst8,dst9,dst10,dst11,dst12,dst13,dst14,dst15,dst16,dst17,dst18,dst19,dst20]


# Find the top 3 smallest, because the smallest value in these calculation is itself  
# So, the second and the third smallest is the two nearest records 

# In[40]:


def smallestdist(euclidean): 
    length = len(euclidean) 
    euclidean.sort() 
    print("Smallest element is:", euclidean[0]) 
    print("Second Smallest element is:", euclidean[1])
    print("Third Smallest element is:",euclidean[2])
smallestdist(euclidean)


# => We see that, the two nearest record are the 15th row and the 20th row
#   
# We do the same thing with Manhattan distance(the other name is Cityblock) 

# In[41]:


dst1 = distance.cityblock(selectRe, row1)
dst2 = distance.cityblock(selectRe,row2)
dst3 = distance.cityblock(selectRe,row3)
dst4 = distance.cityblock(selectRe,row4)
dst5 = distance.cityblock(selectRe,row5)
dst6 = distance.cityblock(selectRe,row6)
dst7 = distance.cityblock(selectRe,row7)
dst8 = distance.cityblock(selectRe,row8)
dst9 = distance.cityblock(selectRe,row9)
dst10 = distance.cityblock(selectRe,row10)
dst11 = distance.cityblock(selectRe,row11)
dst12 = distance.cityblock(selectRe,row12)
dst13 = distance.cityblock(selectRe,row13)
dst14 = distance.cityblock(selectRe,row14)
dst15 = distance.cityblock(selectRe,row15)
dst16 = distance.cityblock(selectRe,row16)
dst17 = distance.cityblock(selectRe,row17)
dst18 = distance.cityblock(selectRe,row18)
dst19 = distance.cityblock(selectRe,row19)
dst20 = distance.cityblock(selectRe,row20)


# In[42]:


print("distance from the selected record to row1=",dst1)
print("distance from the selected record to row2=",dst2)
print("distance from the selected record to row3=",dst3)
print("distance from the selected record to row4=",dst4)
print("distance from the selected record to row5=",dst5)
print("distance from the selected record to row6=",dst6)
print("distance from the selected record to row7=",dst7)
print("distance from the selected record to row8=",dst8)
print("distance from the selected record to row9=",dst9)
print("distance from the selected record to row10=",dst10)
print("distance from the selected record to row11=",dst11)
print("distance from the selected record to row12=",dst12)
print("distance from the selected record to row13=",dst13)
print("distance from the selected record to row14=",dst14)
print("distance from the selected record to row15=",dst15)
print("distance from the selected record to row16=",dst16)
print("distance from the selected record to row17=",dst17)
print("distance from the selected record to row18=",dst18)
print("distance from the selected record to row19=",dst19)
print("distance from the selected record to row20=",dst20)


# In[43]:


manhattan=[dst1,dst2,dst3,dst4,dst5,dst6,dst7,dst8,dst9,dst10,dst11,dst12,dst13,dst14,dst15,dst16,dst17,dst18,dst19,dst20]


# In[44]:


smallestdist(manhattan)


# => We see that, the two nearest record are the 15th row and the 20th row

# ### Q4. (10 bonus pts) Remark the distribution of attribute values in the found records in Q.3, compared with the selected record.

# In[45]:


df.drop(df.index[[0,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18]])


# Remark: The attribute values in the found record and the selected record are very closed 

# In[ ]:




