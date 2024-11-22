# Task 1 - Load and study the data

# Load "numpy" and "pandas" for manipulating numbers and data frames
# Load "matplotlib.pyplot" and "seaborn" for data visualisation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the "winequality-white.csv" file as a Pandas DataFrame
data = pd.read_csv('/content/Wine Quality Dataset.csv')

# Take a brief look at the data
data.head(10)

# Get the dimensions of the dataframe
data.shape

# Get the row names of the dataframe
data.index

# Get the column names of the dataframe
data.columns

# Look at basic information about the dataframe
data.info()

# Create a histogram of the "Quality" feature
plt.figure(figsize = (6,4))
sns.histplot(data = data ,x = 'quality', color = 'purple',
             edgecolor = 'linen', alpha = 0.7, bins = 5)
plt.title("Histogram of Quality")
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()



# Task 2 - View the distributions of the various features in the data set and calculate their central tendencies 


# Calculate the mean of "fixed acidity" feature
round(data['fixed acidity'].mean(),2)


# Calculate the median of "fixed acidity" feature
data['fixed acidity'].median()


# Create a histogram of the "fixed acidity" feature and also show the mean and the median
plt.figure(figsize = (9,4))
sns.histplot(data = data ,x = 'fixed acidity', color = 'orange',
             edgecolor = 'linen', alpha = 0.5, bins = 5)
plt.title("Histogram of Fixed Acidity")
plt.xlabel('Fixed Acidity')
plt.ylabel('Count')
plt.vlines(data['fixed acidity'].mean(), ymin = 0, ymax = 4000, colors='blue', label='Mean')
plt.vlines(data['fixed acidity'].median(), ymin = 0, ymax = 4000, colors='red', label='Median')
plt.legend()
plt.show()


# Create a histogram of the "volatile acidity" feature
plt.figure(figsize = (9,4))
sns.histplot(data = data ,x = 'volatile acidity', color = 'green',
             edgecolor = 'linen', alpha = 0.7, bins = 5)
plt.title("Histogram of Volatile Acidity")
plt.xlabel('Volatile Acidity')
plt.ylabel('Count')
plt.show()


# Plot distplot using 'Volatile acidity' feature
plt.figure(figsize = (9,4))
sns.distplot(data['volatile acidity'], color = 'blue')
plt.title("Distplot of Volatile Acidity")
plt.xlabel('Volatile Acidity')
plt.ylabel('Density')
plt.show()


# Calculate skewness of 'Volatile Acidity'
data['volatile acidity'].skew()
# If Skewness (S) = 0, then the distribution is normally distributed.
# If Skewness (S) > 0, then the distribution is positively skewed.
# If Skewness (S) < 0, then the distribution is negatively skewed.


# Calculate the mean "Volatile Acidity" feature
data['volatile acidity'].mean()


# Calculate the median "Volatile Acidity" feature
data['volatile acidity'].median()


# Create a histogram of the "Volatile Acidity" feature and also show the mean and the median
plt.figure(figsize = (9,4))
sns.histplot(data = data ,x = 'volatile acidity', color = 'green',
             edgecolor = 'linen', alpha = 0.5, bins = 5)
plt.title("Histogram of Volatile Acidity")
plt.xlabel('Volatile Acidity')
plt.ylabel('Density')
plt.vlines(data['volatile acidity'].mean(), ymin = 0, ymax = 3000, colors='blue', label='Mean')
plt.vlines(data['volatile acidity'].median(), ymin = 0, ymax = 3000, colors='red', label='Median')
plt.legend()
plt.show()
# Observations
# The mean and the median are close to each other and the difference between them is very small.
# We can safely choose the mean as the measure of the central tendency here.


quality = pd.DataFrame(data['quality'].value_counts())

# Create a count plot of the "Quality" feature
plt.figure(figsize = (9,4))
sns.barplot(x=quality.index, y=quality.quality)
plt.title("Bar Plot of Quality")
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()

# Count the number of occurences of different categories of the "Quality" feature
data['quality'].value_counts()

# Calculate the mode of the "quality" feature
data['quality'].value_counts().index[0]


# Task 3 - Create a new Pandas Series that contains the details of the acid types for a quality

# Create a new Pandas Series called "rep_acid" that contains the details of the representative quality for the different types of acids
rep_acid = pd.DataFrame(index = ['fixed acidity','volatile acidity','citric acid','quality'],
                     data = [data['fixed acidity'].mean(),data['volatile acidity'].mean(),
                             data['citric acid'].mean(),data['quality'].value_counts().index[0]])

# Print the "rep_acid" series
rep_acid