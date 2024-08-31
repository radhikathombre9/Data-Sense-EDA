# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:07:16 2024

@author: Radhika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Basic Assignments

# Q1. Create a histogram with 50 bins using random normally distributed data. Overlay a KDE plot.

data_hist = np.random.randn(1000)
sns.histplot(data_hist, bins=50, kde=True)
plt.title('Histogram with KDE')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()


# Q2. Generate a scatter plot using random data, with different hues and styles for two categories.

x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)
hue_data = np.random.choice(['Group A', 'Group B'], 100)
style_data = np.random.choice(['Type 1', 'Type 2'], 100)

sns.scatterplot(x=x_scatter, y=y_scatter, hue=hue_data, style=style_data)
plt.title('Scatter Plot with Hue and Style')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

# Intermediate
# You have three lists of random data representing different attributes of movies:
    
genres = ['Action', 'Drama', 'Comedy', 'Thriller', 'Romance', 'Documentary', 
          'Horror', 'Adventure', 'Sci-Fi', 'Biography']*2

budgets = [55, 120, 75, 200, 95, 140, 30, 180, 85, 50, 
           110, 160, 70, 135, 90, 145, 60, 175, 80, 100]

box_office_earnings = [250, 500, 350, 700, 400, 550, 200, 650, 300, 450, 
                       600, 750, 340, 680, 410, 560, 290, 630, 370, 480]
# Create a pandas DataFrame using the three lists, where each genre corresponds to a specific budget and box office earning.
df = pd.DataFrame({
    'Genre': genres,
    'Budget (in millions)': budgets,
    'Box Office Earnings (in millions)': box_office_earnings
})

print(df)


# Generate a box plot using Seaborn to visualize the distribution of box office earnings for each genre.


plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Genre', y='Box Office Earnings (in millions)', palette='pastel')
plt.title('Distribution of Box Office Earnings by Genre')
plt.xlabel('Genre')
plt.ylabel('Box Office Earnings (in millions)')
plt.show()


# Analyze the plot to determine if there are any outliers in the box office earnings for specific genres.
# Thriller and Adventure genres show potential high-end outliers, indicating a few very successful movies.
# Documentary and Horror genres show possible outliers, one on the high end for Documentary and one
# on the low end for Horror.
# Comment on the general trends you observe in the data. 
#           'Horror', 'Adventure', 'Sci-Fi', 'Biography']


    
    
    
    
    
    
    
    
    
    
    
    































