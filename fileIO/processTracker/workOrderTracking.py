# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:15:17 2019

@author: Marshall

take a work order inventory csv file 
filter the data first for oil, then for any additional restictrions
analyze resulting data frames

read/write to excel
pd.read_excel('file.xlsx')
pd.to_excel('dir/myDataFrame.xlsx', sheet_name='Sheet1')

"""
import os
import re
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#create dataframe
df = pd.read_csv("work_order_inventory_SystemDevelopment.csv")

#drop columns that have volume
#volume values are often zero and not relevant
def dropVolumeColumns():
    """
    drop any column from df that is volume based
    """
    columns_to_drop =[]
    for vol in df.columns:
        if vol not in columns_to_drop:
            m = re.search(r"Volume", vol)
            if m:
                columns_to_drop.append(vol)
    df.drop(columns_to_drop, axis=1, inplace = True)

dropVolumeColumns()

def fillEmptyCellsWithNAN():
    """
    fill any empty cells with NAN
    """
    for entry in df.columns:
        df[entry].replace("", np.nan, inplace=True)
        
fillEmptyCellsWithNAN()

df.dropna(axis=0, how='any', inplace=True)

#create a global dataframe that is updated before analysis
working_df = None

#add columns here and drop the rest from dataFrame once filtering is complete
columns_to_use = []

#============================
#print(df_columns)
#    'Database ID', 'WO Name', 'WO Type', 'Location', 'Date Opened',
#   'User Opened', 'Input Bulk Lot ID(s)', 'Input Bulk Lot Type(s)',
#   'Production', 'Input Weight per Bulk Lot', 'Input Volume per Bulk Lot',
#   'Total WO Input Weight', 'Total WO Input Volume', 'Finalized',
#   'Total Finalized Weight', 'Total Finalized Volume',
#   'Output Bulk Lot ID(s)', 'Output Bulk Lot Type(s)', 'Production.1',
#   'Output Weight per Bulk Lot', 'Output Volume per Bulk Lot',
#   'Total Output Weight', 'Total Output Volume', 'Variance Weight %',
#   'Variance Volume %', 'Date Closed', 'User Closed'
#============================

wo_types = []
for item in df["WO Type"]:
    work_order_regex = re.search("Oil", item)
    if item not in wo_types:
        if work_order_regex:
            wo_types.append(item)
#============================
#['Oil - PreDilution', 'Oil - Rotary Evaporation', 'Oil - Winterization/Filtration',
# 'Oil - Extraction', 'Oil - Encapsulation and Sealing', 'Oil - Dilution', 
# 'Oil - Transfer to Extraction Department', 'Oil - Winterization', 
# 'Oil - Decarboxylation', 'Oil - Milling', 'Oil - Final Package (Capsules)', 'Oil - Filtration',
# 'Oil - Mixing to Specific THC:CBD Ratio', 'Oil - Final Package (60 mL Bottle)',
# 'QA Release Cannabis Oil']
#============================

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
def filtering(filteringTerm, colName, dataFrameToFilter):
    """
    """
    bools =[]
    #pattern = re.compile(filteringTerm)
    #create a Pd series for comparison
    for item in dataFrameToFilter[colName]:
        m = re.search(str(filteringTerm), item)#regex 
        if m:#create boolean list to compare
            bools.append(True)
        else:
            bools.append(False)
    boolsSeries = pd.Series(bools, name="bools")#make pd series of booleans
    return (dataFrameToFilter[boolsSeries.values])#return boolean filtered DataFrame
    
    

def plotIt(Xseries, Yseries):
    """
    https://matplotlib.org/users/pyplot_tutorial.html
    """
    plt.xlabel(Xseries.name)
    plt.ylabel(Yseries.name)
    plt.plot(Xseries, Yseries)
    #plt.axis()
    plt.show()

def getDateRange(text_prompt):
    """
    return a date of format dd/mm/yyyy
    input a string to prompt user for a start/end date
    """
    query_date_ok = False
    query_date = None
    
    while not query_date_ok:
        query_date = str(input(f"{text_prompt} (DD/MM/YYYY): "))
        regex = re.search("\S{2}/\S{2}/\S{4}",query_date)
        
        if regex:
            query_date_ok = True
    
    return query_date
    
#======================
#         TESTING
#======================



#filter for only wokrorders that are OIL related
working_df = filtering("Oil", "WO Type", df)
#get start date 
#start_date = getDateRange("Start Date please")
#get end date
#end_date = getDateRange("End Date please")

    
def filterDateRange(start_date, end_date):
    """
    filter data range 
    """
    pass


def getIndependentVariable():
    """
    """
    print("From the following enter an independent variable to analyze")
    for item in working_df.columns:
        print(item)
    
    ind_var = str(input("Enter independent variable: "))
    
    while ind_var not in working_df.columns:
        print("Please enter a valid option from the list provided: ")
        print("=====================")
        for item in working_df.columns:
            print(f"==       {item} ")
        print("=====================")
        ind_var = str(input("Enter independent variable: "))
  
    
def getDependentVariable():
    """
    """
    print("From the following enter an independent variable to analyze")
    for item in working_df.columns:
        print(item)
    
    dep_var = str(input("Enter dependent variable: "))
    
    while dep_var not in working_df.columns:
        print("Please enter a valid option from the list provided: ")
        print("=====================")
        for item in working_df.columns:
            print(f"==       {item} ")
        print("=====================")
        dep_var = str(input("Enter dependent variable: "))


#ind_var = getIndependentVariable()

#dep_var = getDependentVariable()

working_df = filtering("Oil - Extraction", "WO Type", working_df)


def getStatsForSeries(var, write_file = False):
    """
    """
    show = working_df["Total Output Weight"] / working_df["Total WO Input Weight"] #pd series
    #plot a histogram
    plt.hist(show, bins=200)
    plt.show()
    #basic stats given for the process below
    total_mass_input = 0
    for mass in working_df[input_weight]:
        total_mass_input += mass
        total_mass_output = 0
    for omass in working_df[output_weight]:
        total_mass_output += omass
    length = len(var)
    the_sum = 0
    for item in var:
        the_sum +=item
    avg = the_sum / len(var)
    print("======================================")
    print(f"{var} \n\n is {length} items long. Percent yield total = {the_sum}. Average percent yield = {avg*100}%.")
    print(f"Total mass input = {total_mass_input} grams ")
    print(f"Total mass output = {total_mass_output} grams")
    print("======================================")
     
    if write_file:
        file = open("workOrderAnalysis.txt", "w")
        file.write("======================================\n")
        file.write(f"{var} \n\n is {length} items long. Percent yield total = {the_sum}. \nAverage percent yield = {avg*100}%.")
        file.write(f"\nTotal mass input = {total_mass_input} grams ")
        file.write(f"\nTotal mass output = {total_mass_output} grams\n")
        file.write("======================================\n")
        
        file.close()
 
    
        
        
        




this_pattern = "07/12/2018"

first_new_df = filtering(this_pattern, "WO Type", df)#works

second_new_df = filtering(this_pattern, "Date Opened", df)#work

#second argument is causing error
#third_new_df = filtering(this_pattern, "Date Closed", df)# does not work
#error caused by missing data in dataframe
#handling for blank cells required...dropna, replace, ..etc





