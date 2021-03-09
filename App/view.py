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

def print_resultsReq1(ord_vids, sample):
    size = lt.size(ord_vids)
    if size > sample:
        print("Los primeros ", sample, " videos en views son: ")
        i = 1
        while i <= sample:
            video= lt.getElement(ord_vids,i)
            print("Titulo: " + video['title'] + " Fecha tendencia: " +  video["trending_date"]  + " Canal: " + video["channel_title"]+ " Momento de publicacion: " + video["publish_time"] + " Views: "+ str(video["views"]) + " Likes: " + str(video["likes"])+ " Dislikes: " + str(video["dislikes"]))
            i += 1
    else:
        print("La cantidad que desea ver excede la cantidad de videos que desea ver")

def print_resultsReq2(tupla, videos_ordenados):
    dias = tupla[0]
    video_tendencia = tupla[1]
    video = lt.getElement(videos_ordenados, video_tendencia)
    print("Titulo: " + video['title'] + " Nombre del canal: " +  video['channel_title']  + ' País: ' + video['country'] + ' Días: ' + str(dias))

def print_resultsReq3(tupla):
    dias=tupla[1]
    video=tupla[0]
    print("Titulo: " + video['title'] + " Nombre del canal: " +  video['channel_title'] + " Categoria: " + str( video['category_id'])+ " Dias: " + str(dias))

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
        result = controller.sortVideos(filtrado_categoria)
        print("El tiempo (mseg) es: ", str(result[0]))
        print_resultsReq1(result[1], tamano)
        controller.limpieza(filtrado_categoria)
        controller.limpieza(filtrado_pais)
        controller.limpieza(result)

    elif int(inputs[0]) == 3:
        pais = input('Ingrese el pais para el cual desea realizar la búsqueda: ')
        pais = pais.lower()
        filtrado_pais = controller.filtrado_pais(catalog, pais)
        result = controller.sortVideosReq2(filtrado_pais)
        video_tendencia = controller.trendingInCountry(result[1])
        print_resultsReq2(video_tendencia, result[1])
        #print(result[1])
        controller.limpieza(filtrado_pais)
        controller.limpieza(result)

    elif int(inputs[0]) == 4:
        categoria= input("Ingrese la categoria para la cual desea ver el video con mas dias como tendencia: ")
        categoria=categoria.lower()
        categoria= " "+categoria
        lista= controller.lista(catalog)
        cat_num = controller.idCat(catalog, categoria)
        filtro_cat=controller.filtrado_categoria(lista, cat_num)
        orden_id= controller.sortVideosReq2(filtro_cat)
        video_mayor = controller.tendenciaCat(orden_id[1])
        print_resultsReq3(video_mayor)
        controller.limpieza(lista)
        controller.limpieza(filtro_cat)

    elif int(inputs[0]) == 5:
        pais = input("Ingrese el pais para el cual desea realizar la búsqueda: ")
        pais= pais.lower()
        tag= input("Ingrese el tag que desea que buscar")
        filtro_pais=filtrado_pais(catalog, pais)
    else:
        sys.exit(0)
sys.exit(0)
