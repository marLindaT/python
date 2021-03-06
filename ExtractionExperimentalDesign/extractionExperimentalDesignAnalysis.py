# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:46:54 2019

@author: Marshall



experimental design results analysis

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def getData():
    """
    grab user input.Filename string 
    should be csv file
    error handling required
    """
    file_name = str(input("Enter filename of csv file: "))
    if file_name =="":
        df = pd.read_csv("Extraction_experimentalDesignResultsSummary_incomplt.csv", sep=",")
    else:
        df = pd.read_csv(file_name, sep=",")
    return df

#original dataFrame
df = getData()

def cleanInput(dataFr):
    """
    input dataFrame
    return dataFrame 
    """
    for entry in dataFr:
        dataFr[entry].replace("",np.nan, inplace=True)
        
def getColNames(dataFr):
    for entry in dataFr.columns:
        print(entry)
    
def plot3D(X, Y, Z ):
    """
    """
    Axes3D.plot_surface(X, Y, Z, norm=None, vmin=None, vmax=None, lightsource=None)


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')



#=================================
#
#Axes3D.plot_surface(X, Y, Z, *args, norm=None, vmin=None, vmax=None, lightsource=None, **kwargs)[source]
#Create a surface plot.
#
#By default it will be colored in shades of a solid color, but it also supports color mapping by supplying the cmap argument.
#
#Note
#
#The rcount and ccount kwargs, which both default to 50, determine the maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points.
#
#Parameters:	
#X, Y, Z : 2d arrays
#Data values.
#
#rcount, ccount : int
#Maximum number of samples used in each direction. If the input data is larger, it will be downsampled (by slicing) to these numbers of points. Defaults to 50.
#
#New in version 2.0.
#
#rstride, cstride : int
#Downsampling stride in each direction. These arguments are mutually exclusive with rcount and ccount. If only one of rstride or cstride is set, the other defaults to 10.
#
#'classic' mode uses a default of rstride = cstride = 10 instead of the new default of rcount = ccount = 50.
#
#color : color-like
#Color of the surface patches.
#
#cmap : Colormap
#Colormap of the surface patches.
#
#facecolors : array-like of colors.
#Colors of each individual patch.
#
#norm : Normalize
#Normalization for the colormap.
#
#vmin, vmax : float
#Bounds for the normalization.
#
#shade : bool
#Whether to shade the face colors.
#
#**kwargs :
#Other arguments are forwarded to Poly3DCollection.