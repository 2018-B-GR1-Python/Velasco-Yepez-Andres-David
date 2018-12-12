# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:28:05 2018

@author: Andres
"""

import pandas as pd
import os
from functools import reduce

directorio_archivo = 'C://Users//Andres//Documents//GitHub//Velasco-Yepez-Andres-David-Python//03_spyder//data//artwork_data_frame.pickle'
df = pd.read_pickle(directorio_archivo)


df.loc[1035,'artist'] #'Blake, Robert'

#df.loc[0,0] # no sirve no esta basado en cero

df.iloc[0,0] #'Blake, Robert'

df.iloc[0,1]

df.iloc[0,:] # solo la primera fila

#df.iloc[1035,'height']*df.iloc[1035,'width']

a=df['width'].sort_values()
primeros_10=df['width'].sort_values().head(10) # Ordena los valores y saca los primeros 10
ultimos_10=df['width'].sort_values().tail(10) # Ordena los valores y saca los ultimos 10

a=pd.to_numeric(df['width'],errors='coerce') #No tomar los strings y pasarlos a nan
b=pd.to_numeric(df['height'],errors='coerce')
a*b


df.loc[:,'width'] = a
df.iloc[:,6] = b


area = df['width']*df['height']

df = df.assign(area=area) # asignar una nueva columna
df_area = df['area'].sort_values(ascending=False).head(1)
id_aream = df['area'].idxmax()
df.loc[id_aream,:]

reduce(lambda x,y:max(x,y),df['area'].sort_values())

