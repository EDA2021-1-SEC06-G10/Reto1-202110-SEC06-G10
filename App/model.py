"""
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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def dataType(tipo):
    return tipo

def newCatalog(tipo):
    catalog = {'videos': None,
                'channel_title': None,
                'categories': None}
    
    tipos = dataType(tipo)
    catalog['videos'] = lt.newList()
    if tipos == 'ARRAY_LIST':
        catalog['channel_title'] = lt.newList('ARRAY_LIST', cmpfunction=comparechanneltitles)
        catalog['categories'] = lt.newList('ARRAY_LIST', cmpfunction=comparetagnames)
    elif tipos == 'LINKED_LIST':
        catalog['channel_title'] = lt.newList('LINKED_LIST', cmpfunction=comparechanneltitles)
        catalog['categories'] = lt.newList('LINKED_LIST', cmpfunction=comparetagnames)
    return catalog



# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    channel_titles = video['channel_title'].split(',')
    for channel_title in channel_titles:
        addVideoChannel(catalog, channel_title.strip(), video)

def addVideoChannel(catalog, channel_titlename, video):
    channel_titles = catalog['channel_title']
    poschannel_title = lt.isPresent(channel_titles, channel_titlename)
    if poschannel_title > 0:
        channel_title = lt.getElement(channel_titles, poschannel_title)
    else:
        channel_title = newAuthor(channel_titlename)
        lt.addLast(channel_titles, channel_title)
    lt.addLast(channel_title['videos'], video)

def addCategory(catalog, category):
    c = newCategory(category['name'], category['id'])
    lt.addLast(catalog['categories'], c)


# Funciones para creacion de datos

def newAuthor(name):
    channel_title = {'name': '', 'videos': None, 'likes': 0}
    channel_title['name'] = name
    channel_title['videos'] = lt.newList('ARRAY_LIST')
    return channel_title 

def newCategory(category_name, category_id):
    category = {'category_name': '', 'category_id': ''}
    category['category_name'] = category_name
    category['category_id'] = category_id
    return category

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparechanneltitles(channel_title1, channel_title):
    if (channel_title1.lower() in channel_title['name'].lower()):
        return 0
    return -1

def comparetagnames(category_name, category):
    return (category_name == category['name'])
 
def compareviews(video1,video2):
    result = (video1["views"] < video2["views"])
    return result

# Funciones de ordenamiento

def sortVideos(catalog, size, ordenar):
    sub_list = lt.subList(catalog["videos"],0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    if ordenar == "selec":
        sorted_list = sel.sort(sub_list,compareviews)
    elif ordenar == "inser":
        sorted_list = ins.sort(sub_list,compareviews)
    elif ordenar == "shell":
        sorted_list = sa.sort(sub_list,compareviews)
    t2= time.process_time()
    tiempo_ms= (t2-t1)*1000
    return tiempo_ms, sorted_list