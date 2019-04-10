'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


n_radii = 8
n_angles = 36



x = np.linspace(0, 10)
y = np.linspace(0,15)
z = np.linspace(0,1)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z)

plt.show()
