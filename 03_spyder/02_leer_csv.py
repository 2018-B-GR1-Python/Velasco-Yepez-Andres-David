# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:30 2018

@author: Andres
"""


import pandas as pd
import os

path_csv = "C:\\Users\\Andres\\Documents\\GitHub\\Velasco-Yepez-Andres-David-Python\\03_spyder\\data\\artwork_data.csv"

#1) Archivos de texto
#2)Relational Database
#3)Arhivos Binarios


# Cinco primeros datos


columnas_a_utilizar = ['id',
                       'artist',
                       'title',
                       'medium',
                       'year',
                       'acquisitionYear',
                       'height',
                       'width',
                       'units']

data_frame_artwork = pd.read_csv(path_csv,index_col='id',usecols=columnas_a_utilizar)
data_frame_artwork.shape


# Serializacion del Dataframe
# Desearilzacion del Dataframe

data_frame_artwork.to_pickle('C:\\Users\\Andres\\Documents\\GitHub\\Velasco-Yepez-Andres-David-Python\\03_spyder\\data\\artwork_data_frame.pickle')

data_frame_completo = pd.read_pickle('C:\\Users\\Andres\\Documents\\GitHub\\Velasco-Yepez-Andres-David-Python\\03_spyder\\data\\artwork_data_frame.pickle')
