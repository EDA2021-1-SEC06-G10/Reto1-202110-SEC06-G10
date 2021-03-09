﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import shellsort as she
from DISClib.Algorithms.Sorting import quicksort as qui
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
                'categories': None}
    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = lt.newList('ARRAY_LIST', cmpfunction=comparetagnames)
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    c = newCategory(category['name'], category['id'])
    lt.addLast(catalog['categories'], c)

# Funciones para creacion de datos

def newCategory(category_name, category_id):
    category = {'category_name': '', 'category_id': ''}
    category['category_name'] = category_name.lower()
    category['category_id'] = category_id
    return category

# Funciones de consulta/filtrado

def filtrado_pais(catalog, pais):
    lista_pais = lt.newList("ARRAY_LIST")
    for video in lt.iterator(catalog["videos"]):
        if video["country"] == pais:
            lt.addLast(lista_pais, video)
    return lista_pais

def filtrado_categoria(lista, categoria):
    lista_filt_cat= lt.newList("ARRAY_LIST")
    for video in lt.iterator(lista):
        if video["category_id"] == categoria:
            lt.addLast(lista_filt_cat,video)
    return lista_filt_cat

def filtrado_tags_y_pais(catalog, tag, pais):
    lista_tags_y_pais = lt.newList('ARRAY_LIST')
    (tag == '""""""|' + tag + '|""""') or (tag == '""""|' + tag + '|""""') or (tag == '""""|' + tag + '|""""""')
    for video in lt.iterator(catalog['videos']):
        if tag in video['tags'] and video['country'] == pais:
            lt.addLast(lista_tags_y_pais, video)
    return lista_tags_y_pais

def idCat(catalog,categoria):
    num_cat= None
    for kategorien in lt.iterator(catalog["categories"]):
        if categoria== kategorien["category_name"]:
            num_cat = kategorien["category_id"]
    return num_cat

def tendenciaCat(lista):
    size = lt.size(lista)
    top = 0
    i = 0
    while i < size:
        veces = 1
        j = i+1
        centinela = True
        video1= lt.getElement(lista,i)
        while (j < size) and (centinela == True):
            video2 = lt.getElement(lista,j)
            if (video1["video_id"]==video2["video_id"]) and (video1["trending_date"]!= video2["trending_date"]):
                veces+=1
                j+=1
            else:
                centinela = False
                i=j
        if veces > top:
            top=veces
            mayor= video1
        if i==(size-1):
            i+=1
    return (top, mayor)

def trendingInCountry(videos_ordenados):
    posicion = 0
    veces = 1
    mayor = 1
    size = lt.size(videos_ordenados)
    i = 0
    while i < size:
        if i != size:
            id_video = lt.getElement(videos_ordenados, i)
            id_video_2 = lt.getElement(videos_ordenados, i + 1)
            if id_video['video_id'] == id_video_2['video_id']:
                veces += 1
            else: 
                if veces > mayor:
                    mayor = veces
                    posicion = i
                veces = 1
            i += 1
        else:
            if i == size:
                break
    
    video = lt.getElement(videos_ordenados, posicion)
    return (mayor, video)

# Funciones utilizadas para comparar elementos dentro de una lista

def comparechanneltitles(channel_title1, channel_title):
    if (channel_title1.lower() in channel_title['name'].lower()):
        return 0
    return -1

def comparetagnames(category_name, category):
    return (category_name == category['category_name'])
 
def compareviews(video1, video2):
    result = (video1["views"] > video2["views"])
    return result

def compareids(video1, video2):
    result = (video1['video_id'] > video2['video_id'])
    return result

def comparelikes(video1, video2):
    result = (video1['likes'] > video2['likes'])
    return result

def lista(catalog):
    lista= catalog["videos"]
    return lista
# Funciones de ordenamiento

def sortVideos(lista):
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = mer.sort(sub_list, compareviews)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortVideosReq2y3(lista):
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = she.sort(sub_list, compareids)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortVideosReq4(lista):
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = qui.sort(sub_list, comparelikes)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def limpieza(lista):
    lista= None
    return lista