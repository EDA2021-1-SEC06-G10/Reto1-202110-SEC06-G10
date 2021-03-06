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
import time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadCategory(catalog)
    loadVideos(catalog)
    

def loadVideos(catalog):
    videosfile = cf.data_dir + 'GoodReads/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        filtrado= {}
        filtrado["video_id"] = video["video_id"]
        filtrado["trending_date"] = video["trending_date"]
        filtrado["title"] = video["title"]
        filtrado["channel_title"] = video["channel_title"]
        filtrado["category_id"] = int(video["category_id"])
        filtrado["publish_time"] = video["publish_time"]
        filtrado["tags"] = video["tags"]
        filtrado["views"] = int(video["views"])
        filtrado["likes"] = int(video["likes"])
        filtrado["dislikes"] = int(video["dislikes"])
        filtrado["country"] = video["country"]
        #filtrado['trending_time'] = datetime.strptime(video['trending_time'], '%y.%d.%m').date()
        #filtrado['publish_time'] = datetime.strptime(video['publish_time'], '%y.%d.%m').date()
        model.addVideo(catalog, filtrado)

def loadCategory(catalog):
    categoriesfile = cf.data_dir + 'GoodReads/category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for category in input_file:
        category_list = category['id\tname'].split('\t')
        category['name'] = category_list[1]
        category['id'] = int(category_list[0])
        model.addCategory(catalog, category)

# Funciones de ordenamiento

def sortVideos(lista):
    return model.sortVideos(lista)

def sortVideosReq2(lista):
    return model.sortVideosReq2(lista)

def limpieza(lista):
    return model.limpieza(lista)

# Funciones de consulta sobre el catálogo
def filtrado_pais(catalog, pais):
    return model.filtrado_pais(catalog, pais)

def filtrado_categoria(lista, categoria):
    return model.filtrado_categoria(lista, categoria)

def idCat(catalog, categoria):
    num_cat= model.idCat(catalog, categoria)
    return num_cat

def tendenciaCat(lista):
    return model.tendenciaCat(lista)