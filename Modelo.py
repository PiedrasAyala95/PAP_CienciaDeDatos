# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:28:44 2020

@author: Piedras
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from Mylib import mylib
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,precision_score,recall_score)

#%%------------------------------------Modelo 3 --------------------------------------

#%% importacion de los datos a analizar 
#data = pd.read_csv('C:/Users/Piedras-Private/Desktop/5 Semestre/Ciencia de datos/Datos/HR_comma_sep.csv',header = None)
#data.columns = ['Satisfaction','Last Evaluation','Number Project','Average montly','Time spend','Work accident','Left','Promotion 5 years','Sales','Salary']
