# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 06:07:53 2019

@author: Marshall
"""


import pandas as pd

import matplotlib.pyplot as py

import statsmodels.api as sm


age_height = {"CBD": [2, 5, 8, 12, 21, 25],

              "THC":[24, 46, 47, 68, 71, 70.5]}

df = pd.DataFrame(age_height)



py.plot(df["THC"], df["CBD"])



