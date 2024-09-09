# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:20:30 2021

@author: DavidAlcázarSánchez
"""
#lo siguiente indica que tenemos disponible las funciones creadas en el modulo
import Lib_DavidAlcazarSanchez
#Llamamos a la funcion creada pasandole como argumento el numero del ejercicio :)
numEjercicio = 2
Lib_DavidAlcazarSanchez.datosAlumno(numEjercicio)
#-------------------------------------------------------------------
print()
print()

print ("¡Hola! En este programa vas a introducir 10 números, y posteriormente \
       vamos a sacar por pantalla solamente los números impares.")

#Creamos un contador y una lista de números vacía que utilizaremos después.
contador = 0
listaNumeros = []

#Con un while, ejecutamos un bucle hasta que el contador alcance el número de ciclos deseado.
while contador <10:
    #Por cada ciclo, pedimos un número.
    num = int(input("Introduce un número: "))
    #Si ese número está en nuestra lista, nos pedirá otro.
    if num in listaNumeros:
        print("¡Ya has elegido ese número! Elige otro :)")
    #Si no está en nuestra lista, lo añadirá y el contador sumará 1.
    else:    
        listaNumeros += [num]
        contador = contador + 1
        
print()
print (f"La lista de números que has escogido es {listaNumeros}")
print()

#Y con este for que recorre nuestra lista, junto a la condición de que cada número de la lista tenga como resto distinto de cero
#conseguimos sacar los números impares de la misma.
for num in listaNumeros:
    if num % 2 != 0:
        print(f"El número {num} es impar.")