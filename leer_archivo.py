# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:29:27 2024

@author: Dell
"""

noticia = open("noticia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
