"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos")
    print("3- Encontrar tendencia por pais")
    print("4- Encontrar tendencia por categoria")
    print("5- Buscar los videos con mas likes")

def print_results(ord_vids, sample):
    size = lt.size(ord_vids)
    if size > sample:
        print("Los primeros ", sample, " videos en views son: ")
        i = 0
        while i < sample:
            video= lt.getElement(ord_vids,i)
            print("Titulo: " + video['title'] + " Canal: " + video["channel_title"]+ " Views: "+ str(video["views"]))
            i += 1
    else:
        print("la cantidad que desea ver excede la cantidad de videos que desea ver")

def initCatolog():
    return controller.initCatalog()

def dataType(tipo):
    return tipo

def loadData(catalog):
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos .... ")
        t1 = time.process_time_ns()
        catalog = initCatolog()
        loadData(catalog)
        t2 = time.process_time_ns()
        print("El tiempo transcurrido fue: "+ str(t2-t1))
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorías cargadas: ' + str(lt.size(catalog['categories'])))
    elif int(inputs[0]) == 2:
        pais = input("Ingrese el pais para el cual desea realizar la búsqueda: ")
        pais= pais.lower()
        categoria = input("Ingrese la categoria que desea conocer: ")
        categoria= categoria.lower()
        categoria= " "+categoria
        tamano= int(input("Ingrese la cantidad de videos que desea ver: "))
        filtrado_pais = controller.filtrado_pais(catalog, pais)
        num_categoria = controller.idCat(catalog, categoria)
        filtrado_categoria = controller.filtrado_categoria(filtrado_pais, num_categoria)

        result=controller.sortVideos(filtrado_categoria)
        print(result)
        print("El tiempo (mseg) es: ", str(result[0]))
        print_results(result[1], tamano)
        controller.limpieza(result)

    else:
        sys.exit(0)
sys.exit(0)
