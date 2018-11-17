# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import pandas as pd


arreglo_randomico_tres = np.random.rand(3)

arreglo_randomico_2D = np.random.rand(2,3)

# Pandas -> Serie

serie_arreglo = pd.Series(arreglo_randomico_tres)
serie_arreglo_v2 = pd.Series(
                                arreglo_randomico_tres,index=["Uno","Dos","Tres"]
                            )

serie_arreglo.index
serie_arreglo_v2.index


# DataFrames

data_frame = pd.DataFrame(arreglo_randomico_2D)
data_frame[0][0]

data_frame.columns= ['Uno','Dos','Tres']

# [Columna] [Fila]
data_frame['Uno'][0]


