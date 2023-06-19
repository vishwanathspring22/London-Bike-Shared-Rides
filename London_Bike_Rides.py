#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install kaggle')
get_ipython().system('pip install zipfile')


# In[2]:


import zipfile
import pandas as pd
import kaggle


# In[3]:


from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


# In[4]:


get_ipython().system('kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset')


# In[6]:


zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()


# In[7]:


# Read the .csv file as a pandas dataframe 
bike = pd.read_csv("london_merged.csv")


# In[9]:


# explore the data
bike.info()


# In[12]:


# Size and shape of the data
bike.shape

# There are 17,414 rows and 10 attributes in the dataset 


# In[15]:


bike.head(10)


# In[19]:


# count the unique values in the weather_code column
bike.weather_code.value_counts()

# 1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity 
# 2 = scattered clouds / few clouds 
# 3 = Broken clouds 
# 4 = Cloudy 
# 7 = Rain/ light Rain shower/ Light rain 
# 10 = rain with thunderstorm 
# 26 = snowfall 
# 94 = Freezing Fog


# In[18]:


# count the unique values in the season column
bike.season.value_counts()

# "season" - category field meteorological seasons: 
# 0-spring  
# 1-summer  
# 2-fall 
# 3-winter.


# In[22]:


# For clear distinction in Visualization in Tableau in the latter part, Columns are renamed

new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the specified column names
bike.rename(new_cols_dict, axis=1, inplace=True)


# In[23]:


bike


# In[25]:


# changing the humidity values to percentage (i.e. a value between 0 and 1)
bike.humidity_percent = bike.humidity_percent / 100


# In[26]:


# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

# changing the seasons column data type to string
bike.season = bike.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bike.season = bike.season.map(season_dict)

# changing the weather column data type to string
bike.weather = bike.weather.astype('str')
# mapping the values to the actual written weathers
bike.weather = bike.weather.map(weather_dict)


# In[27]:


# checking our dataframe to see if the mappings have worked
bike.head()


# In[28]:


# writing the final dataframe to an excel file that we will use in our Tableau visualisations. 
# The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
bike.to_excel('london_bikes_final.xlsx', sheet_name='Data')





