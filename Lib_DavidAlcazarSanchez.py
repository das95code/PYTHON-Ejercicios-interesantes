# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:38:01 2021

@author: DavidAlcázarSánchez
"""

#Creamos la función que dará los datos del alumno y, según el número que asignemos a la variable "numEjercicio" en cada documento,
#dará el número de ejercicio.
def datosAlumno(numEjercicio):
    print ("Nombre: David")
    print ("Apellidos: Alcázar Sánchez")
    print ("Curso: 1º DAM A") 
    print ("Versión: 2")
           
    if numEjercicio == 1:
        print ("Ejercicio: 1")
           
    if numEjercicio == 2:
        print ("Ejercicio: 2")
        
    if numEjercicio == 3:
        print ("Ejercicio: 3")
        
    if numEjercicio == 4:
        print ("Ejercicio: 4")
        
    if numEjercicio == 5:
        print ("Ejercicio: 5")
 
#Introduzco también en la librería la función "areaCuadrado()", la cual calcula el área del cuadrado y utilizaré en varios ejercicios.        
def areaCuadrado(lado):
    area = lado * lado
    return (area)