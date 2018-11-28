# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 00:03:20 2018

@author: Andres
"""
import pandas as pd
url = 'http://catalogo.datosabiertos.gob.ec/api/action/datastore_search?resource_id=8513f446-1c94-426e-8592-d4cbdd295f33&limit=1000'

datos = pd.read_json(url, typ='frame')
datos =pd.DataFrame.from_dict(datos["result"]["records"]).set_index("_id")


def guardar_bdd():
    global datos
    datos.to_csv('./data/bdd_homicidios.csv', encoding='utf-8')


def consultar(columna, id=None):
    global datos
    #print(datos.loc[int(id),columna])
    return datos.loc[int(id),columna] if id else datos[columna]


def modificar(columna,id,nuevo_valor):
    global datos
    if consultar(columna, id):
        datos.at[int(id),columna] = nuevo_valor
        guardar_bdd()
        return True
    else:
        return False


def eliminar(index):
    global datos
    datos.drop(datos.index[int(index)-1], inplace=True)
    guardar_bdd()


def insertar(Canton,Circuito,Distrito,Edad,Estado_Civil,Fecha_infraccion,Hora_infraccion,Nacionalidad,Provincia,Sexo,Zona,tipo_muert_matriz):
    global datos
    homicidio=Homicidio(Canton,Circuito,Distrito,Edad,Estado_Civil,Fecha_infraccion,Hora_infraccion,Nacionalidad,Provincia,Sexo,Zona,tipo_muert_matriz)
    s = homicidio.get_list()
    serie = pd.Series(s,index=datos.columns)
    datos = datos.append(serie,ignore_index=True)
    guardar_bdd()


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


def menu():
    print("Que desea hacer:")
    print("1. Crear:")
    print("2. Modificar")
    print("3 Consultar")
    print("4. Eliminar")
    opcion = input("Opcion: ")
    if opcion == "1":
        Canton = input("Canton: ")
        Circuito = input("Circuito: ")
        Distrito = input("Distrito: ")
        Edad = input("Edad: ")
        Estado_civil = input("Estado civil: ")
        Fecha_infraccion = input("Fecha infraccion: ")
        Hora_infraccion = input("Hora infraccion: ")
        Nacionalidad = input("Nacionalidad: ")
        Provincia = input("Provincia: ")
        Sexo = input("Sexo: ")
        Zona = input("Zona: ")
        Tipo = input("Tipo: ")
        insertar(Canton, Circuito, Distrito, Edad, Estado_civil, Fecha_infraccion, Hora_infraccion, Nacionalidad,
                 Provincia, Sexo, Zona, Tipo)
    if opcion == "2":
        columna = input("Columna: ")
        id = input("id: ")
        nuevo_valor = input("nuevo_valor: ")
        modificar(columna,id,nuevo_valor)
    if opcion == "3":
        columna = input("Columna: ")
        id = input("id: ")
        print(consultar(columna, id))
    if opcion == "4":
        id = input("id: ")
        eliminar(id)
    menu()

menu()