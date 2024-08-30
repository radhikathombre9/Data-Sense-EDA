# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:51:20 2024

@author: Radhika
"""

import matplotlib.pyplot as plt

# A. Basic Assignments

# Q1. Create a line plot with customized line style, color, and markers.
# Task: Plot the data with a line that is red, dashed, and has circle markers at each data point.

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

plt.plot(x,y, color='red', linestyle="--" , marker='o')
plt.xlabel(x)
plt.ylabel(y)
plt.title('Line plot')
plt.show()

# Q2. Generate a scatter plot using random data and customize the marker size and color.
# Task: Create a scatter plot with blue square markers (s=50) and customize the color to green.

import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x,y, color ='green' , s = 50, marker='s')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("scatter plot")
plt.show()

# B. Intermediate Assignments

# Q1. Create a subplot with 2 rows and 2 columns. In each subplot, plot different types of plots (e.g., line plot, scatter plot, bar plot, and histogram).
# Line
x_line = [0, 1, 2, 3, 4, 5]
y_line = [0, 1, 4, 9, 16, 25]

# scatter
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 3, 5, 7, 11]

# bar
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# histogram
data_hist = np.random.randn(100)

# Task: Create a figure with 2x2 subplots. Plot a line plot, scatter plot, bar plot, 
# and histogram in each of the four subplots


plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.plot(x_line,y_line,color='blue', linestyle='-', marker='o')
plt.title('Line plot')

plt.subplot(2,2,2)
plt.scatter(x_scatter,y_scatter,color='red', marker='s')
plt.title('scatter plot')

plt.subplot(2,2,3)
plt.bar(categories,values,color='green')
plt.title('bar plot')

plt.subplot(2,2,4)
plt.hist(data_hist , bins = 10, color='purple', alpha=0.7)
plt.title('histogram')

plt.tight_layout()
plt.show()


# Q2. Generate a histogram of normally distributed data with customized bin sizes
# ​Task: Create a histogram with 20 bins. Overlay a density plot on the histogram using the same data.

data_histogram = np.random.normal(0, 1, 1000)

plt.hist(data_histogram , bins = 20, color='pink', alpha=0.7, density = True)
plt.title('histogram')
plt.show()


# C. Advanced Assignments

# Q1. Use GridSpec to create a complex figure with at least three different subplots of varying sizes.

# Line Plot:
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 6, 7, 8, 7]

# scatter
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
# Task: Use GridSpec to create a layout with three subplots: a line plot spanning two columns, a bar
 # plot in one column, and a scatter plot below both. Customize each subplot with titles and labels.

import matplotlib.gridspec as gridspec

plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(2, 3)

ax1 = plt.subplot(gs[0, 0:2])  # First row, first two columns
ax2 = plt.subplot(gs[0, 2])    # First row, third column
ax3 = plt.subplot(gs[1, :])    # Second row, all columns

ax1.plot(x_line,y_line)
ax2.bar(categories,values)
ax3.scatter(x_scatter,y_scatter)

ax1.set_title('Plot 1')
ax2.set_title('Plot 2')
ax3.set_title('Plot 3')

plt.show()



# Q2. Create a plot that includes customized ticks, labels, and annotations to highlight key data points.
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

plt.plot(x, y)
plt.annotate('Important Point', xy=(3, 5), xytext=(4, 6),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Plot with Annotation')
plt.show()






