# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:57:16 2019

@author: Marshall
"""


import pandas as pd

import matplotlib.pyplot as plt

dataFrame = pd.read_csv("extractionRunResult_.txt", sep="\t")


def buildPlots():
    counter = 0
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
            
            plt.savefig(f"Charts/extractionChart{counter}.png")
            
            counter+=1
            
            #plt.show()

buildPlots()