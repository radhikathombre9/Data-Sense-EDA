# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:44:11 2024

@author: Radhika
"""

import pandas as pd
import matplotlib.pyplot as plt

# A. Basic Questions

# Create a Pandas Series with 5 elements of your choice. Access the third element.

series = pd.Series([31,32,33,34,35],index=[1,2,3,4,5])
print(series)


# Create a DataFrame from a dictionary with at least 3 columns and 5 rows. Select the first two rows and two columns

df = pd.DataFrame({'roll no':[1,2,3,4,5],
                   'name':['Radha','krishna','Ganesh','Shiv','Laxmi'],
                   'marks':[26,28,29,27,25]})
print(df)

df.iloc[0:2,0:2]


# B. Intermediate Questions

# Import a CSV file into a DataFrame. Drop any rows with missing values and then sort the DataFrame by one of its columns.


data1 = pd.read_csv(r"D:\Nikhil Analytics\Data Sense EDA\Class 2\practice-20240823T073540Z-001\practice\intermediate_practice.csv")
print(data1)

data1 = data1.dropna()
data1 = data1.drop_duplicates()
print(data1)

data_sorted = data1.sort_values(by='Math')
print(data_sorted)

grouped_data = data1.groupby(by = ['Student'])['English'].mean()
print(grouped_data)
grouped_data.plot(kind='bar', color='skyblue')
plt.title('Average Math Scores by Student')
plt.xlabel('Student')
plt.ylabel('Average Math Score')
plt.show()

# C. Advanced Questions

# Merge two DataFrames on a common column. Perform an inner join and an outer join. Explain the differences in the results.
# Given a dataset of customer orders, identify the top 3 customers with the highest total purchase amounts and export this data to a CSV file.

df1 = pd.read_csv(r"D:\Nikhil Analytics\Data Sense EDA\Class 2\practice-20240823T073540Z-001\practice\advanced_practice1.csv")
print(df1)


df2 = pd.read_csv(r"D:\Nikhil Analytics\Data Sense EDA\Class 2\practice-20240823T073540Z-001\practice\advanced_practice2.csv")
print(df2)

merged_df1 = pd.merge(df1,df2,on='CustomerID',how='inner')
print(merged_df1)

merged_df2 = pd.merge(df1,df2,on='CustomerID',how='outer')
print(merged_df2)

#inner join merge only the common record from both the dataframes and outer join merge all the records


















