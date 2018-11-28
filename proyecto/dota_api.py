# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 00:03:20 2018

@author: Andres
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.misc import imread
from urllib.request import urlopen


def getImages_from_urls(urls):
    return list(map(lambda url: imread(urlopen(link+url), mode='RGB'),urls))



url = "https://api.opendota.com/api/heroStats"
link= "https://api.opendota.com"
datos = pd.read_json(url,typ='frame')
print(type(datos))
columnas = ["id","icon","localized_name", "primary_attr", "attack_type",
             "roles", "base_health", "base_health_regen", "base_mana", "base_mana_regen",
             "base_armor", "base_mr", "base_attack_min", "base_attack_max", "base_str",
             "base_agi", "base_int", "str_gain", "agi_gain","int_gain","attack_range",
             "projectile_speed","attack_rate","move_speed","turn_rate"]
datos=datos[columnas].set_index('id')

datos.to_csv('./data/heroes.csv', encoding='utf-8')
datos_ataque_rango = datos.sort_values(by=['attack_range', 'base_attack_max'], ascending=False)

url_icons = datos_ataque_rango['icon'][:10]
arreglo_iconos = getImages_from_urls(url_icons)

plt.title("Diez mejores heroes de rango con el mayor daño")
rects = plt.bar(datos_ataque_rango['localized_name'][:10], datos_ataque_rango['base_attack_max'][:10])
plt.bar(datos_ataque_rango['localized_name'][:10], datos_ataque_rango['base_attack_max'][:10])

plt.show()




