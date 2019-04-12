"""

3d scatter bc i give up trying to get surface to work

"""


import sys

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from numpy.random import randn
from scipy import array, newaxis

import statsmodels.api as sm


df = pd.read_csv("Extraction_experimentalDesignResultsSummary_incomplt.csv", sep=",")


def writeToFile(fileName, text):
    file = open(f"{fileName}.txt", "a")
    file.write(str(text))
    file.close()



#====================
#
#['Experiment Number', 'C3 press', 'C2 press', 'C1 press', 'C1 temp',
#       'C2 temp', 'C3 temp', 'Decarb Cannabinoids % w/w',
#       ' Decarb Water Content % w/w', 'Spent1 Post-Ext. Weight g',
#       'Spent1 Cannabinoids % w/w', 'Spent1 Water Content % w/w',
#       'Spent2 Post-Ext. Weight g', 'Spent2 Cannabinoids % w/w',
#       'Spent2 Water Content % w/w', 

#       'Crude C1 - Weight g',
#       'Crude C2 - Weight g', 'Crude C3 - Weight g',
#       'Crude C1 - Cannabinoids % w/w', 'Crude C2 - Cannabinoids % w/w',
#       'Crude C3 - Cannabinoids % w/w',


#        'Waxes C1 - Dry Weight g',
#       'Waxes C2 - Dry Weight g', 'Waxes C3 - Dry Weight g',


#       'Refined C1 - Weight g', 'Refined C2 - Weight g',
#       'Refined C3 - Weight g',

# ' Refined C1 - Cannabinoids % w/w',
#       ' Refined C2 - Cannabinoids % w/w', ' Refined C3 - Cannabinoids % w/w',

#       'Terpenes Decarb % w/w',
#       'Terpenes Spent %w/w',

# 'Terpenes Crude C1 % w/w',
#       'Terpenes Crude C2 % w/w', 'Terpenes Crude C3 % w/w',
#       'Terpenes Refined C1 % w/w', 'Terpenes Refined C2 % w/w',
#       'Terpenes Refined C3 % w/w'],
#     

#===============================

#==============   CANNABINOIDS

df['sum_crude'] = df['Crude C1 - Weight g'] + df['Crude C2 - Weight g'] + df["Crude C3 - Weight g"]

df["col_1_grams_API"] = (df["Crude C1 - Cannabinoids % w/w"] / 100) * df["Crude C1 - Weight g"]

df["col_2_grams_API"] = (df["Crude C2 - Cannabinoids % w/w"] / 100) * df["Crude C2 - Weight g"]

df["col_3_grams_API"] = (df["Crude C3 - Cannabinoids % w/w"] / 100) * df["Crude C3 - Weight g"]

df["col_1_percent_API_of_total"] = (df["col_1_grams_API"] / df["sum_crude"]) * 100

df["col_2_percent_API_of_total"] = (df["col_2_grams_API"] / df["sum_crude"]) * 100

df["col_3_percent_API_of_total"] = (df["col_3_grams_API"] / df["sum_crude"]) * 100 

collectors_percent_API = [df["col_1_percent_API_of_total"], df["col_2_percent_API_of_total"], df["col_3_percent_API_of_total"]  ]

#================= TERPENES

df["sum_terpenes_crude_grams"] = (df["Crude C1 - Weight g"]*(df["Terpenes Crude C1 % w/w"] / 100)) + (df["Crude C2 - Weight g"]*(df["Terpenes Crude C2 % w/w"] / 100)) + (df["Crude C3 - Weight g"]*(df["Terpenes Crude C3 % w/w"] / 100))

df["col_1_crude_grams_terps"] = df["Crude C1 - Weight g"] * (df["Terpenes Crude C1 % w/w"] / 100)

df["col_2_crude_grams_terps"] = df["Crude C2 - Weight g"] * (df["Terpenes Crude C2 % w/w"] / 100)

df["col_3_crude_grams_terps"] = df["Crude C3 - Weight g"] * (df["Terpenes Crude C3 % w/w"] / 100)

df["col_1_percent_terps_of_total"] = 100 * df["col_1_crude_grams_terps"] / df["sum_terpenes_crude_grams"]

df["col_2_percent_terps_of_total"] = 100 * df["col_2_crude_grams_terps"] / df["sum_terpenes_crude_grams"]

df["col_3_percent_terps_of_total"] = 100 * df["col_3_crude_grams_terps"] / df["sum_terpenes_crude_grams"]

collectors_percent_terps =[df["col_1_percent_terps_of_total"], df["col_2_percent_terps_of_total"], df["col_3_percent_terps_of_total"]  ]


X = df.values[:,2]
Y = df.values[:,5]
Z = df.values[:,19]

def fillBlankWithNan(datafr):
    """
    """
    for item in datafr.columns:
        datafr[item].replace("", np.nan, inplace=True)

def dropNaCols(datafr):
    """
    """
    datafr.dropna(axis="columns", how="all", inplace=True)
    
def dropNaRows(datafr):
    """
    """
    datafr.dropna(axis="rows", how="any", inplace=True)

fillBlankWithNan(df)
dropNaCols(df)
#dropNaRows(df)

def plotLots(arr1,numContinuousRows, saveToFile=False):
    """
    """
    for item in arr1:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        X = df["C1 press"][:numContinuousRows+1]
        Y = df["C1 temp"][:numContinuousRows+1]
        Z = item[:numContinuousRows+1]
        ax.scatter(X, Y, Z)
        ax.set_xlabel(X.name)
        ax.set_ylabel(Y.name)
        ax.set_zlabel(item.name)
        
        if saveToFile:
            plt.savefig(f'{X.name}_{Y.name}_{item.name}_3dscatter.pdf', transparent=True, )
        plt.show()
        
#call
#cannabinoids
plotLots(collectors_percent_API, 8, saveToFile = True)
#terpenes
plotLots(collectors_percent_terps, 8, saveToFile = True)


def regressionAnalysis(datafr, response, var1, var2, var3, var4):
    """
    """
    df =datafr.iloc[:8]
    print(df)
    X = df[[var1, var2, var3, var4]] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
    Y = df[response]

    X = sm.add_constant(X) # adding a constant

    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X) 

    print_model = model.summary()
    
    writeToFile("regression_out", print_model)
    
    print(print_model)
    
regressionAnalysis(df, "col_1_percent_API_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")

regressionAnalysis(df, "col_2_percent_API_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp") 

regressionAnalysis(df, "col_3_percent_API_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")

regressionAnalysis(df, "col_1_percent_terps_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")

regressionAnalysis(df, "col_2_percent_terps_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")

regressionAnalysis(df, "col_3_percent_terps_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")

regressionAnalysis(df, "col_3_percent_terps_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp")


#store dataframe as csv file
df.to_csv(r'dataFrame_out.csv')


