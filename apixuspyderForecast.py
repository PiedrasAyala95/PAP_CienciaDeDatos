# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:44:27 2018

@author: ferur
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from client import ApixuClient, ApixuException
api_key = '6f7c2c38fb0c491ea9502109181810'
client = ApixuClient(api_key)
days_forecast=range(6);
#locations=['Celaya','Irapuato']
locations=['Aguascalientes']


DataFrame={}
i=0;
k=0;


for k in range(len(locations)):
    Nombre=("Date","MAX Temp","MIN Temp","AVG HUMIDITY","UV","MAX WIND","TOTAL PRECIP")
   # Nombre=("Date","MAX Temp","MIN Temp","AVG HUMIDITY","UV","MAX WIND","MIN WIND","TOTAL PRECIP")
    
    sjdr2=client.getForecastWeather( q=str(locations[k]), days=8)
    DataFrame[locations[k]]=pd.DataFrame(np.zeros(((len(Nombre)),len(days_forecast))),index=Nombre)



    for i in days_forecast:
        DataFrame[locations[k]][i]["Date"]=sjdr2['forecast']['forecastday'][i]['date'];
        DataFrame[locations[k]][i]["MAX Temp"]=sjdr2['forecast']['forecastday'][i]['day']['maxtemp_c'];
        DataFrame[locations[k]][i]["MIN Temp"]=sjdr2['forecast']['forecastday'][i]['day']['mintemp_c'];
        DataFrame[locations[k]][i]["AVG Temp"]=sjdr2['forecast']['forecastday'][i]['day']['avgtemp_c'];
        DataFrame[locations[k]][i]["AVG HUMIDITY"]=sjdr2['forecast']['forecastday'][i]['day']['avghumidity']; 
        DataFrame[locations[k]][i]["UV"]=sjdr2['forecast']['forecastday'][i]['day']['uv']; 
        DataFrame[locations[k]][i]["MAX WIND"]=sjdr2['forecast']['forecastday'][i]['day']['maxwind_kph'];          
        #DataFrame[locations[k]][i]["MIN WIND"]=sjdr2['forecast']['forecastday'][i]['day']['minwind_kph'];          
        DataFrame[locations[k]][i]["TOTAL PRECIP"]=sjdr2['forecast']['forecastday'][i]['day']['totalprecip_mm'];          
                  
        
        
        
        
        
                  
                  
                  
                  
                  
                  
                  
                  
                  # a={'Max Grados C*':[sjdr2['forecast']['forecastday'][i]['day']['maxtemp_c']], 
 #  'Min Grados C*':[sjdr2['forecast']['forecastday'][i]['day']['mintemp_c']], 
  # 'Humedad Prom':sjdr2['forecast']['forecastday'][i]['day']['avghumidity'],
   #'Rayos UV':[sjdr2['forecast']['forecastday'][i]['day']['uv']],
   #'Max Viento km/h':[sjdr2['forecast']['forecastday'][i]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
  # 'Precipitacion':[sjdr2['forecast']['forecastday'][i]['day']['totalprecip_mm']]} 
        
     