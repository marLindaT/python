# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:16:23 2019

@author: Marshall
"""

#################
# https://datatofish.com/statsmodels-linear-regression/
#################

import io

import pandas as pd

import statsmodels.api as sm

import matplotlib.pyplot as plt


df = pd.read_csv("extractionRunResult_.txt", sep="\t")



#output from above as column_list
#['UniqueID', 'Strain', 'CBD=1', 'Lot Number', 'Extraction Run',
#       'Time (mins)', 'Col1/2', 'PSI', 'Temp (degC)', 'Program Used 0/1',
#       'Mass CO2 Used lbs', 'Extraction Efficiency THC',
#       'Extraction Efficiency CBD', 'Extraction Efficiency CBN',
#       'Input Mass (g)', 'Output Spent Mass (g)', '% Mass Extracted',
#       'Spent % (as is) THC', 'Spent % (as is) CBD', 'Spent % (as is) CBN',
#       'Decarb % (as is) THC', 'Decarb % (as is) CBD', 'Decarb % (as is) CBN']

column_list = df.columns

X = df["Time (mins)"]
Y = df["Mass CO2 Used lbs"]



#### Ordinary least Squares fitting
model = sm.OLS(Y,X).fit()
#model.predict(X)
model_print = model.summary()
print(print_model)

f = open("extractionPlotsScratch.txt", "w")
f.write(str(print_model))
f.close()

#
#plt.xlabel(X.name)
#plt.ylabel(Y.name)
#plt.title(f"{Y.name} VS {X.name}")
#plt.plot(X, Y , "rd")



def writeToFile(fileName, content):
    
    f = open("extractionPlotsScratch.txt", "w")
    f.write()
    f.close()



def main():

    column_list = df.columns
    
    for first_item in column_list:
        for second_item in column_list:
            
            X = df[first_item]
            Y = df[second_item]
            
            X = sm.add_constant(X)#Adds a column of ones to an array for X
    # Without a constant we are forcing our model to go through the origin
    
    #A simple ordinary least squares mode
    # statsmodels.regression.linear_model.OLS(Yvar, XVar-req add_constant)
    # see https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html
            model = sm.OLS(Y.astype(float), X.astype(float)).fit()
    
            predictions = model.predict(X)
            print_model = model.summary()
        
            file = open("linearRegressionAnalysis.txt", "w")
            
            file.write(model.summary().as_text())
            
            file.close()
    
            print(print_model)

# here we have 2 variables for multiple regression.
# If you just want to use one variable for simple linear 
# regression, then use X = df['Interest_Rate'] for example.
# Alternatively, you may add additional variables within the brackets


##adding a constant
#X = sm.add_constant(X)
#
#model = sm.OLS(Y, X).fit()
#
#predictions = model.predict(X)
#
#print_model = model.summary()
#
#print(print_model)