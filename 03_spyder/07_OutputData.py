# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:16:30 2018

@author: Andres
"""

import pandas as pd
import os
import numpy as np
import sqlite3


directorio_archivo = 'C://Users//Andres//Documents//GitHub//Velasco-Yepez-Andres-David-Python//03_spyder//data//artwork_data_frame.pickle'
data_frame_guardado = pd.read_pickle(directorio_archivo)
seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

with sqlite3.connect('mi_base.db') as conexion:
    seccion_df.to_sql('Artwork',conexion)
    
# JSON    
seccion_df.to_json('artwork.json')
seccion_df.to_json('artwork2.json',orient='table')

# Excel
seccion_df.to_excel("basico.xlsx")
seccion_df.to_excel("basico_sin_indice.xlsx",index=False)
seccion_df.to_excel("solo_algunas_columnas.xlsx",columns=['artist','title','year'])

#Multiples hojas de trabajo
writter = pd.ExcelWriter('multiples_hojas.xlsx',engine='xlsxwriter')

seccion_df.to_excel(writter,sheet_name="Preview",index=False) #Hoja Preview

#Hoja complete todos los datos
data_frame_guardado.to_excel(writter,sheet_name='complete',index=False)
#Guardar todos los archivos
writter.save()


#Formateo Condicional
artistas_contados = data_frame_guardado['artist'].value_counts()
artistas_contados.head()
writer = pd.ExcelWriter('colores.xlsx',engine='xlsxwriter')

artistas_contados.to_excel(writer,sheet_name='Artist Counts')
hoja = writer.sheets['Artist Counts']

cells_range = 'B2:B{}'.format(len(artistas_contados.index))

hoja.conditional_format(cells_range,{
        'type':'2_color_scale',
        'max_type':'percentile',
        'min_value':'10',
        'min_type':'percentile',
        'max_value':'99',
        })


