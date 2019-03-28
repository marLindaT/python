# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:16:23 2019

@author: Marshall
"""
#################
# https://datatofish.com/statsmodels-linear-regression/
#################

import pandas as pd

import statsmodels.api as sm


df = pd.read_csv("extractionRunResult_.txt", sep="\t")

column_list = df.columns

for first_item in column_list:
    for second_item in column_list:
        
        X = df[first_item]
        Y = df[second_item]
        
        X = sm.add_constant(X)

        model = sm.OLS(Y.astype(float), X.astype(float)).fit()

        predictions = model.predict(X)

        print_model = model.summary()

        print(print_model)

# here we have 2 variables for multiple regression.
# If you just want to use one variable for simple linear 
# regression, then use X = df['Interest_Rate'] for example.
# Alternatively, you may add additional variables within the brackets

#X = df[['Interest_Rate','Unemployment_Rate']] 
#Y = df['Stock_Index_Price']
#
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