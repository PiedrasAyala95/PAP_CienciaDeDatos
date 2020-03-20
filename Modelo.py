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

#%% Importamos las bases de datos

Datos_Ameca = pd.read_csv('C:/Users/Piedras/Documents/Github/PAP_CienciaDeDatos/Datos_Clima/Ameca.csv',header=0)
#Datos_Queretaro = pd.read_csv('C:/Users/Piedras/Documents/Github/PAP_CienciaDeDatos/Datos_Clima/Queretaro.csv',header=0)

#%% Hacemos un reporte de las bases de datos para saber si hay datos perdidos o si algo algo raro en ellas

Reporte_Ameca = mylib.mylib.dqr(Datos_Ameca)
#Reporte_Queretaro = mylib.mylib.dqr(Datos_Queretaro)

#%% Agarramos los datos que vamos a modelar, en este caso agarramos los datos de la temperatura maxima.

Col_maxtemp1= Datos_Ameca.iloc[:,1] 
#Col_maxtemp2= Datos_Queretaro.iloc[:,1] 

#%% Hacemos un arreglo con el tiempo del 2009 al 2020

datos_fechas= np.arange(np.datetime64('2009-01-01'), np.datetime64('2020-02-21'))

i = 0
Max_temp1=np.array(np.zeros(4068))
for j in range(4068):
    Max_temp1[j] = Col_maxtemp1[i]
    i=i+24
    
#i = 0   
#Max_temp2=np.array(np.zeros(4068))
#for j in range(4068):
#    Max_temp2[j] = Col_maxtemp2[i]
#    i=i+24
    
 #%% Graficamos
 
plt.hist(Col_maxtemp1)
plt.figure(figsize=(15,10))
plt.plot(datos_fechas,Max_temp1)
plt.title('Movimiento de la Temperatura Maxima')
plt.xlabel('Años')
plt.ylabel('Temperatura')
plt.grid(True)
plt.show()   