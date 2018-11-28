
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 01:15:31 2018

@author: Andres
"""

import pandas as pd
url = 'http://catalogo.datosabiertos.gob.ec/api/action/datastore_search?resource_id=8513f446-1c94-426e-8592-d4cbdd295f33&limit=1000'

datos = pd.read_json(url, typ='frame')
datos =pd.DataFrame.from_dict(datos["result"]["records"]).set_index("_id")
#datos[ datos['Sexo'] != 'MASCULINO' ]
datos.loc[289,'Canton']
class Homicidio:

    def __init__(self,Canton,Circuito,Distrito,Edad,Estado_Civil,Fecha_infraccion,Hora_infraccion,Nacionalidad,Provincia,Sexo,Zona,tipo_muert_matriz):
        self.Canton=Canton
        self.Circuito=Circuito
        self.Distrito=Distrito
        self.Edad = Edad
        self.Estado_civil=Estado_Civil
        self.Fecha_infraccion=Fecha_infraccion
        self.Hora_infraccion=Hora_infraccion
        self.Nacionalidad=Nacionalidad
        self.Provincia = Provincia
        self.Sexo = Sexo
        self.Zona = Zona
        self.tipo = tipo_muert_matriz

    def get_list(self):
        return [self.Canton,self.Circuito,self.Distrito,self.Edad,self.Estado_civil,self.Fecha_infraccion,
                self.Hora_infraccion,self.Nacionalidad,self.Provincia,self.Sexo,self.Zona,self.tipo]

def insertar(Canton,Circuito,Distrito,Edad,Estado_Civil,Fecha_infraccion,Hora_infraccion,Nacionalidad,Provincia,Sexo,Zona,tipo_muert_matriz):
    global datos
    _id = datos.index+1
    homicidio=Homicidio(Canton,Circuito,Distrito,Edad,Estado_Civil,Fecha_infraccion,Hora_infraccion,Nacionalidad,Provincia,Sexo,Zona,tipo_muert_matriz)
    s = homicidio.get_list()
    serie = pd.Series(s,index=datos.columns)
    datos = datos.append(serie,ignore_index=True)   # adding a row
    



insertar("MIAMI",	"CI","W","211","SOLTERO",	"2019-04-05T00:00:00","2015-12-02T23:00:00",	
         "EEUU","FLORIDA","MASCULINO",	"ZONA 80","Asesinatos"
)


    

