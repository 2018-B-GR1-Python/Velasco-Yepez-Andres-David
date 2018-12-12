# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 07:25:45 2018

@author: Andres
"""

import pandas as pd
import os
import numpy as np
from functools import reduce 
import math

directorio_archivo = 'C://Users//Andres//Documents//GitHub//Velasco-Yepez-Andres-David-Python//03_spyder//data//artwork_data_frame.pickle'

data_frame_guardado = pd.read_pickle(directorio_archivo)
seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

## group by
df_agrupado = seccion_df.groupby('artist')

for name,group_fd in df_agrupado:
    #print(name)
    #print(group_fd)
    anio_minimo =   group_fd['acquisitionYear'].min()
    #ancho_minimo =  group_fd['width'].min()
    #altura_minima = group_fd['height'].min()
    print("{}-{}".format(name,anio_minimo))

def llenar_valores_vacios(series):
    valores_contados = series.value_counts()
    if valores_contados.empty:
        return series
    total = 0
    #sumatoria = reduce((lambda x,y: 0 if type(x)== str or type(y)==str else x+y),series)
    #print(int(sumatoria)/series.size)
    valores_mas_utilizados = valores_contados.index[0]
    nuevo_valor = series.fillna(valores_mas_utilizados)
    return nuevo_valor


#seccion_dos_df = seccion_df.iloc[11838:16441,'medium'].copy()

def transformar_df_por_artista(df,campo):
    df_agrupado_artista = seccion_df.groupby('artist')
    #print(df_agrupado_artista)
    ar = []
    for nombre_artista,grupo in df_agrupado_artista:
        df_llenado = grupo.copy()
        df_llenado.loc[:,campo] = llenar_valores_vacios(grupo[campo])
        ar.append(df_llenado)
    return pd.concat(ar)
        #print(df_llenado)

#transformar_df_por_artista(seccion_df,'height')
#transformar_df_por_artista(seccion_df,'width')

df_t = transformar_df_por_artista(seccion_df,'medium')


df_agrupado_titulo = data_frame_guardado.groupby('title')
titulos_contados = df_agrupado_titulo.size().sort_values(ascending = True)
print(titulos_contados)

condicion = lambda x: len(x.index) > 1 #Que se repitan mas de una vez
dub_titles_df = df_agrupado_titulo.filter(condicion)
print(dub_titles_df)
dub_titles_df.sort_values('title',inplace=True)
        