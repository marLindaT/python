# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:27:44 2019

@author: Marshall
"""
###########################
# https://geo-python.github.io/2017/lessons/L7/matplotlib.html
###########################


import pandas as pd

import matplotlib.pyplot as plt

dataFrame = pd.read_csv("matplotlibTrial.txt", sep="\t", skiprows=2)

columnList = dataFrame.columns

for item in columnList:
    print(item)

#define variables to plot
    
x = dataFrame["Mass CO2 Used (lbs)"]

y = dataFrame["% Mass Extracted"]


#################  SIMPLE PLOT

#build plot and store in memory
#  plt.plot(x,y)
# show plot
#  plt.show()

############ MORE PLOT OPTIONS 
## COMENT OUT THE ABOVE PLOT

# data as a red dashed line with circles showing the data points. 
# This comes from the additional ro-- used with plt.plot(). In
# this case, r tells the plt.plot() function to use red color,
# o tells it to show circles at the points, and -- says to use 
# a dashed line. You can use help(plt.plot) to find out more
# about formatting plots. 

plt.plot(x,y,"ro--")

plt.title("Trial Graph")

plt.xlabel("Mass CO2 Used")

plt.ylabel("Percent Mass Extracted")

##add a text annotation to the graph
plt.text(450, 50, "This is a text point")

#  format for plt.axis() is [xmin, xmax, ymin, ymax] 

plt.axis([0,100,0,1.0])


plt.show()

