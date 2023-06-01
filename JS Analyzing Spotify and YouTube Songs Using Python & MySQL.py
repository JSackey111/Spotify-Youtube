#!/usr/bin/env python
# coding: utf-8

# About the project:
# In this project, I work on real-world dataset of Spotify and Youtube combined. This project aims on cleaning the dataset, analyze the given dataset and mining informational quality insights using python and SQL.
# Prerequisites for the Project: 
# 1.    SQL (MYSQL)
# 2.    Excel
# 3.    Python

# Importing libraries and performing data manipulation 

# In[1]:


import pandas as pd


# In[2]:


songs=pd.read_csv('Spotify_Youtuben.csv')
songs.head()


# Eliminate unnecessary columns from the dataset for our analysis by removing Url_spotify, Uri, Key, Url_youtube, and Description.

# In[3]:


songs=songs.drop(['Url_spotify', 'Uri', 'Key', 'Url_youtube','Description'],axis='columns')
songs


# Null Value Analysis: Assessing Data Completeness and Column-wise Null Sum: 
# Examine the dataset for the presence of null values and calculate the total count of null values for each column, providing insights into the data's completeness and potential data quality issues.

# In[4]:


songs.isnull().sum()


# Null Value Handling:
# Manage null values in data for improved data quality and analysis and return dataframe.

# In[5]:


df = pd.DataFrame(songs)

# Select float-type columns
float_columns = df.select_dtypes(include='float')

# Fill float-type columns with the median value
median_values = float_columns.median()
df[float_columns.columns] = float_columns.fillna(median_values)


# Filling onject data types with Non-specified

# In[6]:


columns_to_fill = ['Title', 'Channel', 'Licensed','official_video']
df[columns_to_fill] = df[columns_to_fill].fillna('Non-specified')


# Duplicate Check and First Value Retention: Data Deduplication for Accuracy Identify and eliminate duplicate records in the dataset while retaining the first occurrence of each unique value. This ensures data integrity by removing redundant information and maintaining the original data structure.

# In[7]:


duplicate_records = df.duplicated(keep='first')
df_unique = df[~duplicate_records]


# Convert the duration in milliseconds to minutes, facilitating a clearer comprehension and representation of time intervals in a more user-friendly format.

# In[8]:


df['Duration_ms'] = df['Duration_ms'].apply(lambda x: x / (1000 * 60))


# Change the name of the modified column to "Duration_min" to accurately reflect the conversion from milliseconds to minutes, providing a more descriptive and meaningful representation of the data.

# In[9]:


df = df.rename(columns={'Duration_ms': 'Duration_min'})


# Eliminate track names that are deemed irrelevant and begin with the "?" character, ensuring the dataset only includes relevant and meaningful track information for further analysis or processing.

# In[10]:


df = df[~df['Track'].str.startswith('?')]


# Compute the Energy to Liveness ratio for each track, quantifying the relationship between energy and liveliness attributes. The resulting ratios are then stored in a column named 'EnergyLiveness' for further analysis or interpretation.

# In[11]:


df['EnergyLiveness'] = df['Energy'] / df['Liveness']


# Modify the data type of the 'views' column to float, enabling numerical operations and facilitating its utilization in subsequent analysis or calculations requiring floating-point values

# In[12]:


df['Views'] = df['Views'].astype(float)


# Analyze the 'views' and 'stream' columns to determine the dominant platform (YouTube or Spotify) on which a song track was most played. Create a new column called 'most_playedon' with values 'Spotify' or 'YouTube' indicating the platform with the highest play count for each song track.

# In[13]:


df['most_playedon'] = df.apply(lambda row: 'Spotify' if row['Stream'] > row['Views'] else 'YouTube', axis=1)


# In[ ]:


df['most_playedon'] = df.apply(lambda row: 'Spotify' if row['Stream'] > row['Views'] else 'YouTube', axis=1)


# In[ ]:





# In[14]:


df.describe() # Now, the dataset is supposed to be clean. We can obtain some statistical information


# In[15]:


df.shape # to get the number of columns and rows


# Saving the clean data on the local system 

# In[16]:


import os
os.getcwd()


# In[19]:


df.to_csv('cleaned_dataset.csv')


# In[ ]:




