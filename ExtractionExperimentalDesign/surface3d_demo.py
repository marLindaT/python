'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd

df = pd.read_csv("Extraction_experimentalDesignResultsSummary_incomplt.csv", sep=",")


#================================
# https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html
#=================================

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
z = np.linspace(0, 1, 40)

X, Y, Z = np.meshgrid(x, y, z)


#Z = f(X, Y)

plt.contour(X, Y, Z, colors='black');

plt.contour(X, Y, Z, 20, cmap='RdGy');

plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();
plt.show()






#===========================
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
#============================
#
#def f(x, y):
#    return np.sin(np.sqrt(x ** 2 + y ** 2))
#
#x = np.linspace(-6, 6, 30)
#y = np.linspace(-6, 6, 30)
#
#X, Y = np.meshgrid(x, y)
#Z = f(X, Y)
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(X, Y, Z, 50, cmap='binary')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z');

#==========================


#============= 3D SCATTER ==========
#ax = plt.axes(projection='3d')
#
## Data for three-dimensional scattered points
#zdata = 15 * np.random.random(100)
#xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
#ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
#
#xdata = df["C2 press"]
#ydata = df[" C2 - Cannabinoids % w/w"]
#zdata = df["C2 temp"]
#
#ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
##========= END 3D SCATTER======




#==============================================

#https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#surface plots

#
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#
## Make data.
#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)
#
#X = df["C2 press"]
#Y = df[" C2 - Cannabinoids % w/w"]
#
##X = [-5, 5, 0.25]
##Y = [-5, 5, 0.25]
#
#Z = df["C2 temp"]
#
#X, Y, Z = np.meshgrid(X, Y, Z)
#R = np.sqrt(X**2)
##Z = np.sin(R)
#
#
#
## Plot the surface.
#surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
#
## Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
#
#
#plt.show()
