# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:57:16 2019

@author: Marshall
"""
######################
#  https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html
#####################


from __future__ import print_function
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

#np.random.seed(9876789)


nsample = 100
x = np.linspace(0, 10, 100)
X = np.column_stack((x, x**2))
beta = np.array([1, 0.1, 10])
e = np.random.normal(size=nsample)


X = sm.add_constant(X)
y = np.dot(X, beta) + e



model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

print(dir(results))
















def buildPlots():
    "function draws all possible chart combinations"
    counter = 0
    dataFrame = pd.read_csv("extractionRunResult_.txt", sep="\t")
    columnList = dataFrame.columns
    
    for first_item in columnList:
        for second_item in columnList:
            
            x = dataFrame[first_item]
            
            y = dataFrame[second_item]
                      
            plt.plot(x,y, "ro")
            
            plt.title(f"{x.name} vs {y.name}")
            
            plt.xlabel(f"{x.name}")
            
            plt.ylabel(f"{y.name}")
                                    
            #add a text annotation to the graph
            #plt.text(450, 50, "This is a text point")
            #  format for plt.axis() is [xmin, xmax, ymin, ymax] 
            #plt.axis([0,100,0,100])
            
            #plt.savefig(f"Charts/extractionChart{counter}.png")
            
            counter+=1
            
            #plt.show()

