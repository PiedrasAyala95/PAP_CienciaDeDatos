# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:49:07 2018

@author: ferur
"""
import matplotlib.pyplot as plt
import pandas as pd
from client import ApixuClient, ApixuException
api_key = '6f7c2c38fb0c491ea9502109181810'
client = ApixuClient(api_key)
days_forecast=6;

#Cuidades
GDL=client.getForecastWeather( q="Guadalajara", days=5)
cel=client.getForecastWeather( q="Celaya", days=5)
ira=client.getForecastWeather( q="Irapuato", days=5)
sal=client.getForecastWeather( q="Salamanca", days=5)
gto=client.getForecastWeather( q="Guanajuato", days=5)
leo=client.getForecastWeather( q="León", days=5)
sma=client.getForecastWeather( q="San Miguel de Allende", days=5)
ags=client.getForecastWeather( q="Aguascalientes", days=5)
frs=client.getForecastWeather( q="Fresnillo", days=5)
mat=client.getForecastWeather( q="Matehuala", days=5)
slp=client.getForecastWeather( q="San Luis Potosí", days=5)
zac=client.getForecastWeather( q="Zacatecas", days=5)
apt=client.getForecastWeather( q="Apatzingán", days=5)
patz=client.getForecastWeather( q="Patzcuaro", days=5)
col=client.getForecastWeather( q="Colima", days=5)
vda=client.getForecastWeather( q="Villa de Álvarez", days=5)
tec=client.getForecastWeather( q="Tecoman", days=5)
jiq=client.getForecastWeather( q="Jiquilpan", days=5)
man=client.getForecastWeather( q="Manzanillo", days=5)
more=client.getForecastWeather( q="Morelia", days=5)
zita=client.getForecastWeather( q="Zitacuaro", days=5)
uru=client.getForecastWeather( q="Uruapan", days=5)
zam=client.getForecastWeather( q="Zamora", days=5)
lap=client.getForecastWeather( q="La Piedad", days=5)
chap=client.getForecastWeather( q="Chapala", days=5) 
zap=client.getForecastWeather( q="Zapopan", days=5)
test=client.getForecastWeather( q="Tesistán", days=5)
zapt=client.getForecastWeather( q="Zapotlanejo", days=5)
tlaq=client.getForecastWeather( q="Tlaquepaque", days=5)
ton=client.getForecastWeather( q="Tonala", days=5)
tlaj=client.getForecastWeather( q="Tlajomulco", days=5)
oco=client.getForecastWeather( q="Ocotlán", days=5)
tepa=client.getForecastWeather( q="Tepatitlán", days=5)
amec=client.getForecastWeather( q="Ameca", days=5)
cocu=client.getForecastWeather( q="Cocula", days=5)
aut=client.getForecastWeather( q="Autlan", days=5)
pto=client.getForecastWeather( q="Puerto Vallarta", days=5)
cdg=client.getForecastWeather( q="Ciudad Guzmán", days=5)
ixm=client.getForecastWeather( q="Ixmiquilpan", days=5)
qro=client.getForecastWeather( q="Querétaro", days=5)
tep=client.getForecastWeather( q="Tepic", days=5)
djdl=client.getForecastWeather( q="San Juan de los Lagos", days=5)
ldm=client.getForecastWeather( q="Lagos de Moreno", days=5)
sjdr=client.getForecastWeather( q="San Juan del Río", days=5)


















import pandas as pd
import numpy as np

##Current

a={'Grados C*':[GDL['current']['temp_c']], 'Nubosidad':[GDL['current']['cloud']], 
   'Humedad':[GDL['current']['humidity']],'Rayos UV':[GDL['current']['uv']],
  'Presion Barometrica': [GDL['current']['pressure_mb']],'Viento km/h':[GDL['current']['wind_kph']], 
  'Direccion de Viento': [GDL['current']['wind_dir']], 'Precipitacion Pluvial': [GDL['current']['precip_in']]}
gdl=pd.DataFrame(data=a, index=[GDL['current']['last_updated']])

b={'Grados C*':[cel['current']['temp_c']], 'Nubosidad':[cel['current']['cloud']], 
   'Humedad':[cel['current']['humidity']],'Rayos UV':[cel['current']['uv']],
  'Presion Barometrica': [cel['current']['pressure_mb']],'Viento km/h':[cel['current']['wind_kph']], 
  'Direccion de Viento': [cel['current']['wind_dir']], 'Precipitacion Pluvial': [cel['current']['precip_in']]}
cel=pd.DataFrame(data=b, index=[cel['current']['last_updated']])

c={'Grados C*':[ira['current']['temp_c']], 'Nubosidad':[ira['current']['cloud']], 
   'Humedad':[ira['current']['humidity']],'Rayos UV':[ira['current']['uv']],
  'Presion Barometrica': [ira['current']['pressure_mb']],'Viento km/h':[ira['current']['wind_kph']], 
  'Direccion de Viento': [ira['current']['wind_dir']], 'Precipitacion Pluvial': [ira['current']['precip_in']]}
ira=pd.DataFrame(data=c, index=[ira['current']['last_updated']])

d={'Grados C*':[sal['current']['temp_c']], 'Nubosidad':[sal['current']['cloud']], 
   'Humedad':[sal['current']['humidity']],'Rayos UV':[sal['current']['uv']],
  'Presion Barometrica': [sal['current']['pressure_mb']],'Viento km/h':[sal['current']['wind_kph']], 
  'Direccion de Viento': [sal['current']['wind_dir']], 'Precipitacion Pluvial': [sal['current']['precip_in']]}
sal=pd.DataFrame(data=d, index=[sal['current']['last_updated']])

e={'Grados C*':[gto['current']['temp_c']], 'Nubosidad':[gto['current']['cloud']], 
   'Humedad':[gto['current']['humidity']],'Rayos UV':[gto['current']['uv']],
  'Presion Barometrica': [gto['current']['pressure_mb']],'Viento km/h':[gto['current']['wind_kph']], 
  'Direccion de Viento': [gto['current']['wind_dir']], 'Precipitacion Pluvial': [gto['current']['precip_in']]}
gto=pd.DataFrame(data=e, index=[gto['current']['last_updated']])

e={'Grados C*':[leo['current']['temp_c']], 'Nubosidad':[leo['current']['cloud']], 
   'Humedad':[leo['current']['humidity']],'Rayos UV':[leo['current']['uv']],
  'Presion Barometrica': [leo['current']['pressure_mb']],'Viento km/h':[leo['current']['wind_kph']], 
  'Direccion de Viento': [leo['current']['wind_dir']], 'Precipitacion Pluvial': [leo['current']['precip_in']]}
leo=pd.DataFrame(data=e, index=[leo['current']['last_updated']])

e={'Grados C*':[sma['current']['temp_c']], 'Nubosidad':[sma['current']['cloud']], 
   'Humedad':[sma['current']['humidity']],'Rayos UV':[sma['current']['uv']],
  'Presion Barometrica': [sma['current']['pressure_mb']],'Viento km/h':[sma['current']['wind_kph']], 
  'Direccion de Viento': [sma['current']['wind_dir']], 'Precipitacion Pluvial': [sma['current']['precip_in']]}
sma=pd.DataFrame(data=e, index=[sma['current']['last_updated']])

e={'Grados C*':[ags['current']['temp_c']], 'Nubosidad':[ags['current']['cloud']], 
   'Humedad':[ags['current']['humidity']],'Rayos UV':[ags['current']['uv']],
  'Presion Barometrica': [ags['current']['pressure_mb']],'Viento km/h':[ags['current']['wind_kph']], 
  'Direccion de Viento': [ags['current']['wind_dir']], 'Precipitacion Pluvial': [ags['current']['precip_in']]}
ags=pd.DataFrame(data=e, index=[ags['current']['last_updated']])

e={'Grados C*':[frs['current']['temp_c']], 'Nubosidad':[frs['current']['cloud']], 
   'Humedad':[frs['current']['humidity']],'Rayos UV':[frs['current']['uv']],
  'Presion Barometrica': [frs['current']['pressure_mb']],'Viento km/h':[frs['current']['wind_kph']], 
  'Direccion de Viento': [frs['current']['wind_dir']], 'Precipitacion Pluvial': [frs['current']['precip_in']]}
frs=pd.DataFrame(data=e, index=[frs['current']['last_updated']])

e={'Grados C*':[mat['current']['temp_c']], 'Nubosidad':[mat['current']['cloud']], 
   'Humedad':[mat['current']['humidity']],'Rayos UV':[mat['current']['uv']],
  'Presion Barometrica': [mat['current']['pressure_mb']],'Viento km/h':[mat['current']['wind_kph']], 
  'Direccion de Viento': [mat['current']['wind_dir']], 'Precipitacion Pluvial': [mat['current']['precip_in']]}
mat=pd.DataFrame(data=e, index=[mat['current']['last_updated']])

e={'Grados C*':[slp['current']['temp_c']], 'Nubosidad':[slp['current']['cloud']], 
   'Humedad':[slp['current']['humidity']],'Rayos UV':[slp['current']['uv']],
  'Presion Barometrica': [slp['current']['pressure_mb']],'Viento km/h':[slp['current']['wind_kph']], 
  'Direccion de Viento': [slp['current']['wind_dir']], 'Precipitacion Pluvial': [slp['current']['precip_in']]}
slp=pd.DataFrame(data=e, index=[slp['current']['last_updated']])

e={'Grados C*':[zac['current']['temp_c']], 'Nubosidad':[zac['current']['cloud']], 
   'Humedad':[zac['current']['humidity']],'Rayos UV':[zac['current']['uv']],
  'Presion Barometrica': [zac['current']['pressure_mb']],'Viento km/h':[zac['current']['wind_kph']], 
  'Direccion de Viento': [zac['current']['wind_dir']], 'Precipitacion Pluvial': [zac['current']['precip_in']]}
zac=pd.DataFrame(data=e, index=[zac['current']['last_updated']])

e={'Grados C*':[apt['current']['temp_c']], 'Nubosidad':[apt['current']['cloud']], 
   'Humedad':[apt['current']['humidity']],'Rayos UV':[apt['current']['uv']],
  'Presion Barometrica': [apt['current']['pressure_mb']],'Viento km/h':[apt['current']['wind_kph']], 
  'Direccion de Viento': [apt['current']['wind_dir']], 'Precipitacion Pluvial': [apt['current']['precip_in']]}
apt=pd.DataFrame(data=e, index=[apt['current']['last_updated']])

e={'Grados C*':[patz['current']['temp_c']], 'Nubosidad':[patz['current']['cloud']], 
   'Humedad':[patz['current']['humidity']],'Rayos UV':[patz['current']['uv']],
   'Presion Barometrica': [patz['current']['pressure_mb']],'Viento km/h':[patz['current']['wind_kph']], 
   'Direccion de Viento': [patz['current']['wind_dir']], 'Precipitacion Pluvial': [patz['current']['precip_in']]}
patz=pd.DataFrame(data=e, index=[patz['current']['last_updated']])

e={'Grados C*':[col['current']['temp_c']], 'Nubosidad':[col['current']['cloud']], 
   'Humedad':[col['current']['humidity']],'Rayos UV':[col['current']['uv']],
   'Presion Barometrica': [col['current']['pressure_mb']],'Viento km/h':[col['current']['wind_kph']], 
   'Direccion de Viento': [col['current']['wind_dir']], 'Precipitacion Pluvial': [col['current']['precip_in']]}
col=pd.DataFrame(data=e, index=[col['current']['last_updated']])

e={'Grados C*':[vda['current']['temp_c']], 'Nubosidad':[vda['current']['cloud']], 
   'Humedad':[vda['current']['humidity']],'Rayos UV':[vda['current']['uv']],
   'Presion Barometrica': [vda['current']['pressure_mb']],'Viento km/h':[vda['current']['wind_kph']], 
   'Direccion de Viento': [vda['current']['wind_dir']], 'Precipitacion Pluvial': [vda['current']['precip_in']]}
patz=pd.DataFrame(data=e, index=[vda['current']['last_updated']])

e={'Grados C*':[tec['current']['temp_c']], 'Nubosidad':[tec['current']['cloud']], 
   'Humedad':[tec['current']['humidity']],'Rayos UV':[tec['current']['uv']],
   'Presion Barometrica': [tec['current']['pressure_mb']],'Viento km/h':[tec['current']['wind_kph']], 
   'Direccion de Viento': [tec['current']['wind_dir']], 'Precipitacion Pluvial': [tec['current']['precip_in']]}
tec=pd.DataFrame(data=e, index=[tec['current']['last_updated']])

e={'Grados C*':[jiq['current']['temp_c']], 'Nubosidad':[jiq['current']['cloud']], 
   'Humedad':[jiq['current']['humidity']],'Rayos UV':[jiq['current']['uv']],
   'Presion Barometrica': [jiq['current']['pressure_mb']],'Viento km/h':[jiq['current']['wind_kph']], 
   'Direccion de Viento': [jiq['current']['wind_dir']], 'Precipitacion Pluvial': [jiq['current']['precip_in']]}
jiq=pd.DataFrame(data=e, index=[jiq['current']['last_updated']])

e={'Grados C*':[man['current']['temp_c']], 'Nubosidad':[man['current']['cloud']], 
   'Humedad':[man['current']['humidity']],'Rayos UV':[man['current']['uv']],
   'Presion Barometrica': [man['current']['pressure_mb']],'Viento km/h':[man['current']['wind_kph']], 
   'Direccion de Viento': [man['current']['wind_dir']], 'Precipitacion Pluvial': [man['current']['precip_in']]}
man=pd.DataFrame(data=e, index=[man['current']['last_updated']])

e={'Grados C*':[more['current']['temp_c']], 'Nubosidad':[more['current']['cloud']], 
   'Humedad':[more['current']['humidity']],'Rayos UV':[more['current']['uv']],
   'Presion Barometrica': [more['current']['pressure_mb']],'Viento km/h':[more['current']['wind_kph']], 
   'Direccion de Viento': [more['current']['wind_dir']], 'Precipitacion Pluvial': [more['current']['precip_in']]}
more=pd.DataFrame(data=e, index=[more['current']['last_updated']])

e={'Grados C*':[zita['current']['temp_c']], 'Nubosidad':[zita['current']['cloud']], 
   'Humedad':[zita['current']['humidity']],'Rayos UV':[zita['current']['uv']],
   'Presion Barometrica': [zita['current']['pressure_mb']],'Viento km/h':[zita['current']['wind_kph']], 
   'Direccion de Viento': [zita['current']['wind_dir']], 'Precipitacion Pluvial': [zita['current']['precip_in']]}
zita=pd.DataFrame(data=e, index=[zita['current']['last_updated']])

e={'Grados C*':[uru['current']['temp_c']], 'Nubosidad':[uru['current']['cloud']], 
   'Humedad':[uru['current']['humidity']],'Rayos UV':[uru['current']['uv']],
   'Presion Barometrica': [uru['current']['pressure_mb']],'Viento km/h':[uru['current']['wind_kph']], 
   'Direccion de Viento': [uru['current']['wind_dir']], 'Precipitacion Pluvial': [uru['current']['precip_in']]}
uru=pd.DataFrame(data=e, index=[uru['current']['last_updated']])

e={'Grados C*':[zam['current']['temp_c']], 'Nubosidad':[zam['current']['cloud']], 
   'Humedad':[zam['current']['humidity']],'Rayos UV':[zam['current']['uv']],
   'Presion Barometrica': [zam['current']['pressure_mb']],'Viento km/h':[zam['current']['wind_kph']], 
   'Direccion de Viento': [zam['current']['wind_dir']], 'Precipitacion Pluvial': [zam['current']['precip_in']]}
zam=pd.DataFrame(data=e, index=[zam['current']['last_updated']])

e={'Grados C*':[lap['current']['temp_c']], 'Nubosidad':[lap['current']['cloud']], 
   'Humedad':[lap['current']['humidity']],'Rayos UV':[lap['current']['uv']],
   'Presion Barometrica': [lap['current']['pressure_mb']],'Viento km/h':[lap['current']['wind_kph']], 
   'Direccion de Viento': [lap['current']['wind_dir']], 'Precipitacion Pluvial': [lap['current']['precip_in']]}
lap=pd.DataFrame(data=e, index=[lap['current']['last_updated']])

e={'Grados C*':[chap['current']['temp_c']], 'Nubosidad':[chap['current']['cloud']], 
   'Humedad':[chap['current']['humidity']],'Rayos UV':[chap['current']['uv']],
   'Presion Barometrica': [chap['current']['pressure_mb']],'Viento km/h':[chap['current']['wind_kph']], 
   'Direccion de Viento': [chap['current']['wind_dir']], 'Precipitacion Pluvial': [chap['current']['precip_in']]}
chap=pd.DataFrame(data=e, index=[chap['current']['last_updated']])

e={'Grados C*':[zap['current']['temp_c']], 'Nubosidad':[zap['current']['cloud']], 
   'Humedad':[zap['current']['humidity']],'Rayos UV':[zap['current']['uv']],
   'Presion Barometrica': [zap['current']['pressure_mb']],'Viento km/h':[zap['current']['wind_kph']], 
   'Direccion de Viento': [zap['current']['wind_dir']], 'Precipitacion Pluvial': [zap['current']['precip_in']]}
zap=pd.DataFrame(data=e, index=[zap['current']['last_updated']])

e={'Grados C*':[test['current']['temp_c']], 'Nubosidad':[test['current']['cloud']], 
   'Humedad':[test['current']['humidity']],'Rayos UV':[test['current']['uv']],
   'Presion Barometrica': [test['current']['pressure_mb']],'Viento km/h':[test['current']['wind_kph']], 
   'Direccion de Viento': [test['current']['wind_dir']], 'Precipitacion Pluvial': [test['current']['precip_in']]}
test=pd.DataFrame(data=e, index=[test['current']['last_updated']])

e={'Grados C*':[zapt['current']['temp_c']], 'Nubosidad':[zapt['current']['cloud']], 
   'Humedad':[zapt['current']['humidity']],'Rayos UV':[zapt['current']['uv']],
   'Presion Barometrica': [zapt['current']['pressure_mb']],'Viento km/h':[zapt['current']['wind_kph']], 
   'Direccion de Viento': [zapt['current']['wind_dir']], 'Precipitacion Pluvial': [zapt['current']['precip_in']]}
zapt=pd.DataFrame(data=e, index=[zapt['current']['last_updated']])

e={'Grados C*':[tlaq['current']['temp_c']], 'Nubosidad':[tlaq['current']['cloud']], 
   'Humedad':[tlaq['current']['humidity']],'Rayos UV':[tlaq['current']['uv']],
   'Presion Barometrica': [tlaq['current']['pressure_mb']],'Viento km/h':[tlaq['current']['wind_kph']], 
   'Direccion de Viento': [tlaq['current']['wind_dir']], 'Precipitacion Pluvial': [tlaq['current']['precip_in']]}
tlaq=pd.DataFrame(data=e, index=[tlaq['current']['last_updated']])

e={'Grados C*':[ton['current']['temp_c']], 'Nubosidad':[ton['current']['cloud']], 
   'Humedad':[ton['current']['humidity']],'Rayos UV':[ton['current']['uv']],
   'Presion Barometrica': [ton['current']['pressure_mb']],'Viento km/h':[ton['current']['wind_kph']], 
   'Direccion de Viento': [ton['current']['wind_dir']], 'Precipitacion Pluvial': [ton['current']['precip_in']]}
ton=pd.DataFrame(data=e, index=[ton['current']['last_updated']])

e={'Grados C*':[tlaj['current']['temp_c']], 'Nubosidad':[tlaj['current']['cloud']], 
   'Humedad':[tlaj['current']['humidity']],'Rayos UV':[tlaj['current']['uv']],
   'Presion Barometrica': [tlaj['current']['pressure_mb']],'Viento km/h':[tlaj['current']['wind_kph']], 
   'Direccion de Viento': [tlaj['current']['wind_dir']], 'Precipitacion Pluvial': [tlaj['current']['precip_in']]}
tlaj=pd.DataFrame(data=e, index=[tlaj['current']['last_updated']])

e={'Grados C*':[oco['current']['temp_c']], 'Nubosidad':[oco['current']['cloud']], 
   'Humedad':[oco['current']['humidity']],'Rayos UV':[oco['current']['uv']],
   'Presion Barometrica': [oco['current']['pressure_mb']],'Viento km/h':[oco['current']['wind_kph']], 
   'Direccion de Viento': [oco['current']['wind_dir']], 'Precipitacion Pluvial': [oco['current']['precip_in']]}
oco=pd.DataFrame(data=e, index=[oco['current']['last_updated']])

e={'Grados C*':[tepa['current']['temp_c']], 'Nubosidad':[tepa['current']['cloud']], 
   'Humedad':[tepa['current']['humidity']],'Rayos UV':[tepa['current']['uv']],
   'Presion Barometrica': [tepa['current']['pressure_mb']],'Viento km/h':[tepa['current']['wind_kph']], 
   'Direccion de Viento': [tepa['current']['wind_dir']], 'Precipitacion Pluvial': [tepa['current']['precip_in']]}
tepa=pd.DataFrame(data=e, index=[tepa['current']['last_updated']])

e={'Grados C*':[amec['current']['temp_c']], 'Nubosidad':[amec['current']['cloud']], 
   'Humedad':[amec['current']['humidity']],'Rayos UV':[amec['current']['uv']],
   'Presion Barometrica': [amec['current']['pressure_mb']],'Viento km/h':[amec['current']['wind_kph']], 
   'Direccion de Viento': [amec['current']['wind_dir']], 'Precipitacion Pluvial': [amec['current']['precip_in']]}
amec=pd.DataFrame(data=e, index=[amec['current']['last_updated']])

e={'Grados C*':[cocu['current']['temp_c']], 'Nubosidad':[cocu['current']['cloud']], 
   'Humedad':[cocu['current']['humidity']],'Rayos UV':[cocu['current']['uv']],
   'Presion Barometrica': [cocu['current']['pressure_mb']],'Viento km/h':[cocu['current']['wind_kph']], 
   'Direccion de Viento': [cocu['current']['wind_dir']], 'Precipitacion Pluvial': [cocu['current']['precip_in']]}
cocu=pd.DataFrame(data=e, index=[cocu['current']['last_updated']])

e={'Grados C*':[aut['current']['temp_c']], 'Nubosidad':[aut['current']['cloud']], 
   'Humedad':[aut['current']['humidity']],'Rayos UV':[aut['current']['uv']],
   'Presion Barometrica': [aut['current']['pressure_mb']],'Viento km/h':[aut['current']['wind_kph']], 
   'Direccion de Viento': [aut['current']['wind_dir']], 'Precipitacion Pluvial': [aut['current']['precip_in']]}
aut=pd.DataFrame(data=e, index=[aut['current']['last_updated']])

e={'Grados C*':[pto['current']['temp_c']], 'Nubosidad':[pto['current']['cloud']], 
   'Humedad':[pto['current']['humidity']],'Rayos UV':[pto['current']['uv']],
   'Presion Barometrica': [pto['current']['pressure_mb']],'Viento km/h':[pto['current']['wind_kph']], 
   'Direccion de Viento': [pto['current']['wind_dir']], 'Precipitacion Pluvial': [pto['current']['precip_in']]}
pto=pd.DataFrame(data=e, index=[pto['current']['last_updated']])

e={'Grados C*':[cdg['current']['temp_c']], 'Nubosidad':[cdg['current']['cloud']], 
   'Humedad':[cdg['current']['humidity']],'Rayos UV':[cdg['current']['uv']],
   'Presion Barometrica': [cdg['current']['pressure_mb']],'Viento km/h':[cdg['current']['wind_kph']], 
   'Direccion de Viento': [cdg['current']['wind_dir']], 'Precipitacion Pluvial': [cdg['current']['precip_in']]}
cdg=pd.DataFrame(data=e, index=[cdg['current']['last_updated']])

e={'Grados C*':[ixm['current']['temp_c']], 'Nubosidad':[ixm['current']['cloud']], 
   'Humedad':[ixm['current']['humidity']],'Rayos UV':[ixm['current']['uv']],
   'Presion Barometrica': [ixm['current']['pressure_mb']],'Viento km/h':[ixm['current']['wind_kph']], 
   'Direccion de Viento': [ixm['current']['wind_dir']], 'Precipitacion Pluvial': [ixm['current']['precip_in']]}
ixm=pd.DataFrame(data=e, index=[ixm['current']['last_updated']])

e={'Grados C*':[qro['current']['temp_c']], 'Nubosidad':[qro['current']['cloud']], 
   'Humedad':[qro['current']['humidity']],'Rayos UV':[qro['current']['uv']],
   'Presion Barometrica': [qro['current']['pressure_mb']],'Viento km/h':[qro['current']['wind_kph']], 
   'Direccion de Viento': [qro['current']['wind_dir']], 'Precipitacion Pluvial': [qro['current']['precip_in']]}
qro=pd.DataFrame(data=e, index=[qro['current']['last_updated']])

e={'Grados C*':[tep['current']['temp_c']], 'Nubosidad':[tep['current']['cloud']], 
   'Humedad':[tep['current']['humidity']],'Rayos UV':[tep['current']['uv']],
   'Presion Barometrica': [tep['current']['pressure_mb']],'Viento km/h':[tep['current']['wind_kph']], 
   'Direccion de Viento': [tep['current']['wind_dir']], 'Precipitacion Pluvial': [tep['current']['precip_in']]}
tep=pd.DataFrame(data=e, index=[tep['current']['last_updated']])

e={'Grados C*':[djdl['current']['temp_c']], 'Nubosidad':[djdl['current']['cloud']], 
   'Humedad':[djdl['current']['humidity']],'Rayos UV':[djdl['current']['uv']],
   'Presion Barometrica': [djdl['current']['pressure_mb']],'Viento km/h':[djdl['current']['wind_kph']], 
   'Direccion de Viento': [djdl['current']['wind_dir']], 'Precipitacion Pluvial': [djdl['current']['precip_in']]}
djdl=pd.DataFrame(data=e, index=[djdl['current']['last_updated']])

e={'Grados C*':[ldm['current']['temp_c']], 'Nubosidad':[ldm['current']['cloud']], 
   'Humedad':[ldm['current']['humidity']],'Rayos UV':[ldm['current']['uv']],
   'Presion Barometrica': [ldm['current']['pressure_mb']],'Viento km/h':[ldm['current']['wind_kph']], 
   'Direccion de Viento': [ldm['current']['wind_dir']], 'Precipitacion Pluvial': [ldm['current']['precip_in']]}
ldm=pd.DataFrame(data=e, index=[ldm['current']['last_updated']])

e={'Grados C*':[sjdr['current']['temp_c']], 'Nubosidad':[sjdr['current']['cloud']], 
   'Humedad':[sjdr['current']['humidity']],'Rayos UV':[sjdr['current']['uv']],
   'Presion Barometrica': [sjdr['current']['pressure_mb']],'Viento km/h':[sjdr['current']['wind_kph']], 
   'Direccion de Viento': [sjdr['current']['wind_dir']], 'Precipitacion Pluvial': [sjdr['current']['precip_in']]}
sjdr=pd.DataFrame(data=e, index=[sjdr['current']['last_updated']])

GDL2=client.getForecastWeather( q="Guadalajara", days=5)
cel2=client.getForecastWeather( q="Celaya", days=5)
ira2=client.getForecastWeather( q="Irapuato", days=5)
sal2=client.getForecastWeather( q="Salamanca", days=5)
gto2=client.getForecastWeather( q="Guanajuato", days=5)
leo2=client.getForecastWeather( q="León", days=5)
sma2=client.getForecastWeather( q="San Miguel de Allende", days=5)
ags2=client.getForecastWeather( q="Aguascalientes", days=5)
frs2=client.getForecastWeather( q="Fresnillo", days=5)
mat2=client.getForecastWeather( q="Matehuala", days=5)
slp2=client.getForecastWeather( q="San Luis Potosí", days=5)
zac2=client.getForecastWeather( q="Zacatecas", days=5)
apt2=client.getForecastWeather( q="Apatzingán", days=5)
patz2=client.getForecastWeather( q="Patzcuaro", days=5)
col2=client.getForecastWeather( q="Colima", days=5)
vda2=client.getForecastWeather( q="Villa de Álvarez", days=5)
tec2=client.getForecastWeather( q="Tecoman", days=5)
jiq2=client.getForecastWeather( q="Jiquilpan", days=5)
man2=client.getForecastWeather( q="Manzanillo", days=5)
more2=client.getForecastWeather( q="Morelia", days=5)
zita2=client.getForecastWeather( q="Zitacuaro", days=5)
uru2=client.getForecastWeather( q="Uruapan", days=5)
zam2=client.getForecastWeather( q="Zamora", days=5)
lap2=client.getForecastWeather( q="La Piedad", days=5)
chap2=client.getForecastWeather( q="Chapala", days=5) 
zap2=client.getForecastWeather( q="Zapopan", days=5)
test2=client.getForecastWeather( q="Tesistán", days=5)
zapt2=client.getForecastWeather( q="Zapotlanejo", days=5)
tlaq2=client.getForecastWeather( q="Tlaquepaque", days=5)
ton2=client.getForecastWeather( q="Tonala", days=5)
tlaj2=client.getForecastWeather( q="Tlajomulco", days=5)
oco2=client.getForecastWeather( q="Ocotlán", days=5)
tepa2=client.getForecastWeather( q="Tepatitlán", days=5)
amec2=client.getForecastWeather( q="Ameca", days=5)
cocu2=client.getForecastWeather( q="Cocula", days=5)
aut2=client.getForecastWeather( q="Autlan", days=5)
pto2=client.getForecastWeather( q="Puerto Vallarta", days=5)
cdg2=client.getForecastWeather( q="Ciudad Guzmán", days=5)
ixm2=client.getForecastWeather( q="Ixmiquilpan", days=5)
qro2=client.getForecastWeather( q="Querétaro", days=5)
tep2=client.getForecastWeather( q="Tepic", days=5)
djdl2=client.getForecastWeather( q="San Juan de los Lagos", days=5)
ldm2=client.getForecastWeather( q="Lagos de Moreno", days=5)
sjdr2=client.getForecastWeather( q="San Juan del Río", days=8)

## Forecast



i=0;

for i in days_forecast:
     a={'Max Grados C*':[sjdr2['forecast']['forecastday'][i]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][i]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][i]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][i]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][i]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][i]['day']['totalprecip_mm']]} 

    






















b={'Max Grados C*':[sjdr2['forecast']['forecastday'][1]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][1]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][1]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][1]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][1]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][1]['day']['totalprecip_mm']]} 

c={'Max Grados C*':[sjdr2['forecast']['forecastday'][2]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][2]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][2]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][2]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][2]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][2]['day']['totalprecip_mm']]}

d={'Max Grados C*':[sjdr2['forecast']['forecastday'][3]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][3]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][3]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][3]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][3]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][3]['day']['totalprecip_mm']]}

e={'Max Grados C*':[sjdr2['forecast']['forecastday'][4]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][4]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][4]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][4]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][4]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][4]['day']['totalprecip_mm']]}

f={'Max Grados C*':[sjdr2['forecast']['forecastday'][5]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][5]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][5]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][5]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][5]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][5]['day']['totalprecip_mm']]}

g={'Max Grados C*':[sjdr2['forecast']['forecastday'][6]['day']['maxtemp_c']], 
   'Min Grados C*':[sjdr2['forecast']['forecastday'][6]['day']['mintemp_c']], 
   'Humedad Prom':sjdr2['forecast']['forecastday'][6]['day']['avghumidity'],
   'Rayos UV':[sjdr2['forecast']['forecastday'][6]['day']['uv']],
   'Max Viento km/h':[sjdr2['forecast']['forecastday'][6]['day']['maxwind_kph']], 
   #'Min Viento km/h':[sjdr2['forecast']['forecastday'][0]['day']['minwind_kph']],
   'Precipitacion':[sjdr2['forecast']['forecastday'][6]['day']['totalprecip_mm']]}



index=pd.DataFrame([[sjdr2['forecast']['forecastday'][0]['date']],
                         [sjdr2['forecast']['forecastday'][1]['date']],
                         [sjdr2['forecast']['forecastday'][2]['date']],
                         [sjdr2['forecast']['forecastday'][3]['date']],
                         [sjdr2['forecast']['forecastday'][4]['date']],
                         [sjdr2['forecast']['forecastday'][5]['date']],
                         [sjdr2['forecast']['forecastday'][6]['date']]])

sjdr2=pd.DataFrame(data=[a,b,c,d,e,f,g],index=index)


del(a,b,c,d,e,f,g)

