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

def print_results(ord_vids, sample=10):
    size = lt.size(ord_vids)
    if size > sample:
        print("Los primeros ", sample, " videos en views son: ")
        i = 0
        while i <= sample:
            video= lt.getElement(ord_vids,i)
            print("Titulo: " + video['title'] + " Canal: " + video["channel_title"]+ " Views: "+ video["views"])
            i += 1

def initCatolog():
    return controller.initCatalog()


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
        estructuraDeDatos = input('Ingrese el tipo de estructura de datos quiere usar: ')
        print("Cargando información de los archivos ....")
        t1 = time.process_time_ns()
        catalog = initCatolog()
        loadData(catalog)
        t2 = time.process_time_ns()
        print("El tiempo transcurrido fue: "+ str(t2-t1))
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Canales autores cargados: ' + str(lt.size(catalog['channel_title'])))
        print('Categorías cargadas: ' + str(lt.size(catalog['categories'])))

    elif int(inputs[0]) == 2:
        algoritmo = int(input('Ingrese el tipo de algoritmo quiere usar (1)selection (2)insertion (3)shell: '))
        size = int(input("Ingrese el tamaño de la muestra: "))
        if algoritmo == 1:
            par_algoritmo = "selec"
        elif algoritmo == 2:
            par_algoritmo = "inser"
        elif algoritmo == 3:
            par_algoritmo = "shell"
        result = controller.sortVideos(catalog,size,par_algoritmo)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        print_results(result[1])
    else:
        sys.exit(0)
sys.exit(0)
