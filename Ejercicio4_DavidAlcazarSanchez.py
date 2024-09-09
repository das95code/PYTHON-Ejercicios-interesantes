# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:09:03 2021

@author: DavidAlcázarSánchez
"""
#Importamos como siempre la librería para indicar el número de ejercicio.
import Lib_DavidAlcazarSanchez
#De la librería functools importaremos la función reduce, con la que trabajaremos.
from functools import reduce

#Pintamos como en cada ejercicio los datos del alumno y el número de ejercicio :)
numEjercicio = 4

Lib_DavidAlcazarSanchez.datosAlumno(numEjercicio)

#Creamos listas vacías que llenaremos y utilizaremos más tarde.
listaEstancias = []
listaAnchos = []
listaLargos = []
listaAreas = []
listaEstanciasOculta =[]

#Pedimos el número de habitaciones que tendrá nuestra vivienda.
nHabitaciones = int(input("¿Cuántas habitaciones tiene la casa?: "))

#Por cada número en el rango 1, número de habitaciones +1...
for n in range(1, nHabitaciones+1):
    
    #Se nos preguntará el nombre de la estancia, el largo y el ancho.
    estancia = input("Introduce el nombre de la estancia: ")
    largo = int(input(f"Introduce el largo de {estancia}: "))
    ancho = int(input(f"Introduce el ancho de {estancia}: "))
    
    #Guardaremos toda la información pedida en las listas creadas antes, tanto junta (en una lista que mostraremos en pantalla)
    #Como separada en una serie de listas con las que operaremos nosotros.
    listaEstancias += [(estancia, largo, ancho)]
    listaEstanciasOculta += [estancia]
    listaAreas += [(largo * ancho)]
    listaAnchos += [ancho]
    listaLargos += [largo]
    
    #La listaEstancias simplemente sirve para mostrar en pantalla una lista con todas las estancias.
print("-------------------------------------------")    
print(f"Tu lista de estancias es: {listaEstancias}")
print("-------------------------------------------")

#Definimos la función suma, que utilizaremos en la función reduce posteriormente...
def suma(a,b):
    suma = a + b
    return suma

#Y creamos la variable suma areas que contendrá el valor del resultado de aplicar la función reduce (un sumatorio de todos los valores de las areas)
sumaAreas = reduce(suma, listaAreas)

#Pintamos el área total de las viviendas...
print("El área total de la vivienda es de", sumaAreas, "m2")

#Y posteriormente, con un bucle for y con la función zip, recorreremos, esta vez, tres variables al mismo tiempo de las listas listaEstanciasOculta, listaAnchos y listaLargos
for estancia, ancho, largo in zip(listaEstanciasOculta, listaAnchos, listaLargos):
    #Para poder mostrar la información pedida :)
    print("La estancia", estancia, "tiene", ancho*largo, "m2.")