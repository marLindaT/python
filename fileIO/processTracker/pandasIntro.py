# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:27:44 2019

@author: Marshall
"""

import pandas as pd

import matplotlib.pyplot as plt

#use Pandas to read the txt file
# pd.read_csv()general function for reading data files separated by commas, spaces, or other common separators. We use it her by simply giving the name of the file to read
dataFrame = pd.read_csv("weatherData.txt")

print(dataFrame)

# there are some strange values present such as NaN. 
# NaN stands for not a number, and might indicate some
# problem with reading in the contents of the file. 
# Plus, we expected about 30 lines of data, but the
# index values go up to 36 when we print the contents 
# of dataFrame. Looks like we need to investigate. We 
# can double check the contents of the data stored in
# dataFrame using the Spyder editor panel. If you 
# right-click on the data file name in the File explorer 
# you can select Edit to view the temperature data file 
# in the editor.

#There is some metadata at the top of the file giving basic 
#information about its contents and source. This isn’t
# data we want to process, so we need to skip over that 
# part of the file when we load it. Fortunately, that’s easy
# to do in Pandas, we just need to add the skiprows parameter
# when we read the file, listing the number of rows to 
# skip (8 in this case).

dataFrame = pd.read_csv("weatherData.txt", skiprows=8)

print(dataFrame)

#we have the rows labeled with an index value (0 to 29),
# and columns labelled YEARMODA, TEMP, MAX, and MIN. 
# This is nice because we can easily use these labels to
# divide up our data and make interacting with it 



# how many rows you have, you can use the len()
print(len(dataFrame.index))

# get a quick sense of the size of the dataset using the shape attribute

print(dataFrame.shape)

# select a single column of the data using the column name
print(dataFrame['TEMP'])

#column from a DataFrame is called a Series in Pandas. 
#A Pandas Series is just a 1-D list of values. In fact,
# you can create a Pandas Series from a Python list. If
# you have long lists of numbers, for instance, creating
# a Pandas Series will allow you to interact with these
# values more efficiently in terms of computing time.

type(dataFrame['TEMP'])

myList = [1,2,3,4,5,6,7.0]

# converted to a Pandas Series using the ps.Series()

mySeries = pd.Series(myList)

print(mySeries)



# Pandas Series have a set of attributes they know about 
# themselves and methods they can use to make calculations
# using the Series data. Useful methods include mean(), 
# median(), min(), max(), and std() (the standard deviation)

print(dataFrame["TEMP"].mean())

#useful function to get an overview of the basic statistics
# for all attributes in your DataFrame is the describe() 
# function.

print(dataFrame.describe())

#
# convert data in a Series to another data type. If you’re
# planning to print a large number of value to the screen, 
# for instance, it might be helpful to have those values as 
# character strings. Data type conversions is most easily 
# done using the astype() method.


print(dataFrame['TEMP'].astype(str))

print(dataFrame['TEMP'].astype(int))


