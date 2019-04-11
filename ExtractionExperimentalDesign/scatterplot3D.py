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




#====================
#
#['Experiment Number', 'C3 press', 'C2 press', 'C1 press', 'C1 temp',
#       'C2 temp', 'C3 temp', 'Decarb Cannabinoids % w/w',
#       ' Water Content % w/w', 'Spent Ex-1 Post-Ext. Weight g',
#       ' Ex-1 Cannabinoids % w/w', ' Ex-1 Water Content % w/w',
#       ' Ex-2 Post-Ext. Weight g', ' Ex-2 Cannabinoids % w/w',
#       ' Ex-2 Water Content % w/w', 'Crude C1 - Weight g', ' C2 - Weight g',
#       ' C3 - Weight g', ' C1 - Cannabinoids % w/w',
#       ' C2 - Cannabinoids % w/w', ' C3 - Cannabinoids % w/w',
#       ' C1 - Pictures Mark "complete" when taken',
#       ' C2 - Pictures Mark "complete" when taken',
#       ' C3 - Pictures Mark "complete" when taken', 'Waxes C1 - Dry Weight g',
#       ' C2 - Dry Weight g', ' C3 - Dry Weight g', 'Refined C1 - Weight g',
#       ' C2 - Weight g.1', ' C3 - Weight g.1', ' C1 - Cannabinoids % w/w.1',
#       ' C2 - Cannabinoids % w/w.1', ' C3 - Cannabinoids % w/w.1',
#       ' C1 - Pictures Mark "complete" when taken.1',
#       ' C2 - Pictures Mark "complete" when taken.1',
#       ' C3 - Pictures Mark "complete" when taken.1',
#       'Terpenes Decarb High THC  % w/w',
#       ' Spent (pooled) High THC-EXP02-Spent N/A', ' Crude C1 % w/w',
#       '  C2 % w/w', '  C3 % w/w', ' Refined C1 % w/w', '  C2 % w/w.1',
#       '  C3 % w/w.1', 'Unnamed: 44']

#===============================

df['sum_crude'] = df['Crude C1 - Weight g'] + df[' C2 - Weight g'] + df[" C3 - Weight g"]

df["col_1_grams_API"] = (df[" C1 - Cannabinoids % w/w"] / 100) * df["Crude C1 - Weight g"]

df["col_2_grams_API"] = (df[" C2 - Cannabinoids % w/w"] / 100) * df[" C2 - Weight g"]

df["col_3_grams_API"] = (df[" C3 - Cannabinoids % w/w"] / 100) * df[" C3 - Weight g"]


df["col_1_percent_API_of_total"] = (df["col_1_grams_API"] / df["sum_crude"]) * 100

df["col_2_percent_API_of_total"] = (df["col_2_grams_API"] / df["sum_crude"]) * 100

df["col_3_percent_API_of_total"] = (df["col_3_grams_API"] / df["sum_crude"]) * 100 

collectors_percent_API = [df["col_1_percent_API_of_total"], df["col_2_percent_API_of_total"], df["col_3_percent_API_of_total"]  ]


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
dropNaRows(df)

def plotLots(arr1,numContinuousRows, saveToFile=False):
    """
    """
    for item in arr1:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        X = df["C1 press"]
        Y = df["C2 press"]
        Z = item[:numContinuousRows]
        ax.scatter(X, Y, Z)
        ax.set_xlabel(X.name)
        ax.set_ylabel(Y.name)
        ax.set_zlabel(item.name)
        
        if saveToFile:
            plt.savefig(f'{X.name}_{Y.name}_{item.name}_3dscatter.pdf', transparent=True, )
        plt.show()
#call
plotLots(collectors_percent_API, 8, saveToFile = True)


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
    print(print_model)
    
regressionAnalysis(df, "col_1_percent_API_of_total", "C1 press", "C1 temp", "C2 press", "C2 temp") 
        


df.to_csv(r'dataFrame_out.csv')
