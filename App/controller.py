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
 """

import config as cf
import model
import csv
from time import time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initCatalog(tipo):
    dataType(tipo)
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadCategory(catalog)
    loadVideos(catalog)
    

def loadVideos(catalog):
    videosfile = cf.data_dir + 'GoodReads/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        filtrado= {}
        filtrado["video_id"] = video["video_id"]
        filtrado["trending_date"] = video["trending_date"]
        filtrado["title"] = video["title"]
        filtrado["channel_title"] = video["channel_title"]
        filtrado["category_id"] = video["category_id"]
        filtrado["publish_time"] = video["publish_time"]
        filtrado["tags"] = video["tags"]
        filtrado["views"] = video["views"]
        filtrado["likes"] = video["likes"]
        filtrado["dislikes"] = video["dislikes"]
        filtrado["country"] = video["country"]

        #video['trending_date'] = (filtrado['trending_time']) # FALTA LO DEL TIEMPO
        #video['publish_time'] = (filtrado['publish_time']) # FALTA LO DEL TIEMPO
        video['views'] = int(filtrado['views'])
        video['likes'] = int(filtrado['likes'])
        video['dislikes'] = int(filtrado['dislikes'])
        model.addVideo(catalog, filtrado)

def loadCategory(catalog):
    categoriesfile = cf.data_dir + 'GoodReads/category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        category_list = category['id\tname'].split('\t')
        category['name'] = category_list[1]
        category['id'] = category_list[0]
        model.addCategory(catalog, category)

def dataType(tipo):
    return model.dataType(tipo)

# Funciones de ordenamiento

def sortVideos(catalog, size, ordenar):
    return model.sortVideos(catalog, size, ordenar)

def limpieza(lista):
    return model.limpieza(lista)

# Funciones de consulta sobre el catálogo
