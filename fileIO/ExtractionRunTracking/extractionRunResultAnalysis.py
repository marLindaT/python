# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:20:12 2019

@author: marshall


"""

#import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


def getInputFile():
    """
    take user input string that specifies a csv file
    return a dataframe of the csv data
    """
    file = str(input("Enter filename: "))
    if not file == "":
        return pd.read_csv(file, sep=",")
    else :
        return pd.read_csv("extractionRunResult_.csv", sep=",")
    
df = getInputFile()

#replace all blanks in CBD=1 column as they are ommited during operation if 0
df["CBD=1"].replace(np.nan, 0, inplace = True)

def fillEmptyCellsWithNAN():#this function may not be correct....
    """
    catch empty strings and replace with NaN
    """
    for entry in df.columns:
        df[entry].replace("", np.nan, inplace=True)
        
fillEmptyCellsWithNAN()


#=========================================
#df.columns
#Index(['UniqueID', 'Strain', 'CBD=1', 'Lot Number', 'Extraction Run',
#       'Time (mins)', 'Col1/2', 'PSI', 'Temp (degC)', 'Program Used 0/1',
#       'Mass CO2 Used (lbs)', 'Extraction Efficiency THC',
#       'Extraction Efficiency CBD', 'Extraction Efficiency CBN',
#       'Input Mass (g)', 'Output Spent Mass (g)', '% Mass Extracted',
#       'Spent % (as is) THC', 'Spent % (as is) CBD', 'Spent % (as is) CBN',
#       'Decarb % (as is) THC', 'Decarb % (as is) CBD', 'Decarb % (as is) CBN'],
#      dtype='object')
#=========================================

def getColumn(type_str):
    """
    prompt for a column selection
    return string of column name
    """
    choice_ok = False
    column_to_return = None
    
    while not choice_ok:
        if column_to_return in df.columns:
            choice_ok = True
            break
        else:
            print("=================")
            for item in df.columns:
                print(item)
            print("=================")
            column_to_return = str(input(f"Choose column ({type_str}) : " ))
    return column_to_return

indep_var = getColumn("independent")
dep_var = getColumn("dependent")

def createDataFrame(in_df,var1, var2):
    """
    input sourceDataFrame and two variables
    return a DataFrame of the two variables
    """
    d = {f'{var1}': in_df[var1], f'{var2}': in_df[var2]}
    return pd.DataFrame(data=d)


#create a smaller DF with only columns of interest
working_df = createDataFrame(df, indep_var, dep_var)


def plotTwoColDF(dataframe):
    """
    """
    variable_list = []
    for item in dataframe.columns:
        variable_list.append(item)
    print("=======================\n")    
    print(f"Plotting results for:\n Independent = {variable_list[0]}\n Dependent={variable_list[1]} \n")
    print("=======================\n")  
    plt.plot(dataframe[variable_list[0]], dataframe[variable_list[1]],"go")
    
    model = sm.OLS(dataframe[variable_list[1]], dataframe[variable_list[0]]) #condense into return line
    return model
        
    
model = plotTwoColDF(working_df)    

results = model.fit()
print(results.params)











