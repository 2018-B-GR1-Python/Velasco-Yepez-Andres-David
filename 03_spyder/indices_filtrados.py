# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:48:03 2018

@author: Andres
"""

import pandas as pd
import  os

directorio_archivo = 'C://Users//Andres//Documents//GitHub//Velasco-Yepez-Andres-David-Python//03_spyder//data//artwork_data_frame.pickle'

df_guardado = pd.read_pickle(directorio_archivo)
artistas_df_duplicados = df_guardado['artist']
artistas_df = pd.unique(artistas_df_duplicados)

artistas_bacon_francias = df_guardado['artist'] == 'Bacon, Francis'


# Cuantos valores de este tipo de valor existen
artistas_bacon_francias.value_counts()

# Otra forma

serie_artistas = df_guardado['artist'].value_counts()

# Otra forma de hacer
serie_artistas['Bacon, Francis']

# Otra forma de hacer
len(df_guardado[artistas_bacon_francias])
