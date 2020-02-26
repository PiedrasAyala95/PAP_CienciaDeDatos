# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:28:44 2020

@author: Piedras
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import Mylib as mylib
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (accuracy_score,precision_score,recall_score)

#%%

Datos_Ameca = pd.read_csv('C:/Users/Piedras/Documents/Github/PAP_CienciaDeDatos/Datos_Clima/Ameca.csv',header=0)
Reporte_Ameca = mylib.mylib.dqr(Datos_Ameca)

Col_maxtemp= Datos_Ameca.iloc[:,1] 

#%%

datos_fechas= np.arange(np.datetime64('2009-01-01'), np.datetime64('2020-02-21'))

i = 0
Max_temp =np.array(np.zeros(4068))
for j in range(4068):
    Max_temp[j] = Col_maxtemp[i]
    i=i+24
    
 #%%
plt.figure(figsize=(15,10))
plt.plot(datos_fechas,Max_temp,linewidth=0.7)
plt.title('Movimiento de la Temperatura Maxima')
plt.xlabel('Años')
plt.ylabel('Temperatura')
plt.grid(True)
plt.show()   