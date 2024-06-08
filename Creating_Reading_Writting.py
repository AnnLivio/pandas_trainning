'''
This notebook is an exercise in the [Pandas](https://www.kaggle.com/learn/pandas) course. 
You can reference the tutorial at [this link](https://www.kaggle.com/residentmario/creating-reading-and-writing).**
'''

# Introduction
# The first step in most data analytics projects is reading the data file. 
# In this exercise, you'll create Series and DataFrame objects, both by hand and by reading data files.
#Run the code cell below to load libraries you will need (including code to check your answers).
import pandas as pd
pd.set_option('display.max_rows', 5)


# Exercises
# 1. In the cell below, create a DataFrame `fruits`.
fruits = pd.DataFrame({'Apples':[30], 'Bananas':[21]})

# 2. Create a dataframe `fruit_sales`
fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21,34]}, index=['2017 Sales', '2018 Sales'])

# 3. Create a variable `ingredients` with a Series that looks like:
'''
Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object
'''
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour','Milk','Eggs','Spam'], name='Dinner')

# 4. Read the following csv dataset of wine reviews into a DataFrame called `reviews`:
# The filepath to the csv file is `../input/wine-reviews/winemag-data_first150k.csv`. The first few lines look like:
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# 5. Run the cell below to create and display a DataFrame called `animals`:
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

# In the cell below, write code to save this DataFrame to disk as a csv file with the name `cows_and_goats.csv`.
animals.to_csv("cows_and_goats.csv")
