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


df = pd.read_csv("Book1.csv", sep=",")

X = df.values[:,0]
Y = df.values[:,1]
Z = df.values[:,2]


fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

ax.scatter(X, Y, Z)

plt.show()
