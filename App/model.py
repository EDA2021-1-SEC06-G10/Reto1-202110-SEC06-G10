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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def catalogo():
    catalogo = {'videos': None,
               'categorias': None}
    catalogo["videos"]= lt.newList()
    catalogo["categorias"]= lt.newList("ARRAY_LIST", cmpfunction=comparecate)
    return catalogo

# Funciones para agregar informacion al catalogo
def add_video(catalogo,video):
    lt.addLast(catalogo["videos"],video)
    addCatVid(catalogo, video)

def add_category(catalogo,categoria):
    c= new_category(categoria["name"], categoria["id"])
    lt.addLast(catalogo["categorias"],c)

def addCatVid(catalogo,video):
    categoria=video["category_id"]
    elemento= encontrar_categoria(catalogo,categoria)
    lt.addLast(elemento["videos"], video)

# Funciones para creacion de datos
def new_category(name, identificador):
    categoria= {'name': '', 'tag_id': '', "videos":None}
    categoria["videos"]= lt.newList('ARRAY_LIST')
    categoria["name"]= name.lower()
    categoria["tag_id"]= identificador
    return categoria
# Funciones de consulta
def encontrar_categoria(catalogo, categoria): 
    categoria=categoria
    consulta= lt.isPresent(catalogo["categorias"], categoria)
    elemento = lt.getElement(catalogo["categorias"],consulta)
    return elemento

# Funciones utilizadas para comparar elementos dentro de una lista
def comparecate(categoria1, categoria):
    
    if (categoria1 in categoria["id"]):
        return 0
    return -1 

# Funciones de ordenamiento