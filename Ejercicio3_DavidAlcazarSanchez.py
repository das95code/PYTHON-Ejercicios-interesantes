# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:35:37 2021

@author: DavidAlcázarSánchez
"""
#lo siguiente indica que tenemos disponible las funciones creadas en el módulo
import Lib_DavidAlcazarSanchez
#Llamamos a la funcion creada pasandole como argumento el numero del ejercicio :)
numEjercicio = 3

Lib_DavidAlcazarSanchez.datosAlumno(numEjercicio)

#Pintamos el menú del programa.
print("""---------------------------MENU---------------------------------------
---- 1. - Área (en metros) comprendida entre dos cuadrados         ---
---- 2. - Área de 'n' cuadrados cuyo lado sean los primeros impares---
---- 0. - Salir                                                    ---
----------------------------------------------------------------------""")

#Pedimos con un input (int) un número para elegir la opción. 
opcion = int(input("Introduzca una opción: "))

#Con distintos if, comprobaremos que opción ha sido elegida y ejecutará una parte u otra del programa.
if opcion == 1:
    print ("Vamos a calcular el área en metros comprendida entre dos cuadrados.")
    #Pedimos el lado del primer cuadrado
    lado = int(input("Introduce el valor para el lado del primer cuadrado: "))
    #Y aplicamos la función que tenemos guardada en nuestra librería.
    areaCuadrado1 = Lib_DavidAlcazarSanchez.areaCuadrado(lado)
    #Lo mismo para el segundo cuadrado.
    lado = int(input("Introduce el valor para el lado del segundo cuadrado: "))
    areaCuadrado2 = Lib_DavidAlcazarSanchez.areaCuadrado(lado)
    
    print(f"El área del primer cuadrado es de {areaCuadrado1} m2.")
    print(f"El área del segundo cuadrado es de {areaCuadrado2} m2.")
    
    #Puede darse que el primer cuadrado sea más grande que el segundo o viceversa. Para solventar este error, mediante
    #dos if podremos calcular la diferencia independientemente de qué cuadrado sea más grande que otro.
    if areaCuadrado1 > areaCuadrado2:
        print(f"La diferencia entre las áreas de los cuadrados es de {areaCuadrado1 - areaCuadrado2} m2")
        
    if areaCuadrado2 > areaCuadrado1:
        print(f"La diferencia entre las áreas de los cuadrados es de {areaCuadrado2 - areaCuadrado1} m2")

#Segunda opción del programa.        
if opcion == 2:
    #Lista vacía que usaremos más tarde.
    listaImpares = []
    print ("Vamos a calcular el área de 'n' cuadrados cuyo lado sean los primeros impares.")
    #Pedimos la cantidad de impares con los que queremos operar.
    primerosImpares = int(input("Introduce la cantidad de primeros impares que quieres utilizar: "))
    
    #Con este bucle for, podremos recorrer un rango desde 1 hasta el doble de los impares pedidos (se guardarán números de dos en dos
    #en la lista, de ahí lo de el doble de los pedidos.)
    for num in range (1, (primerosImpares * 2 + 1)):
        if num % 2 != 0:
            #Llenamos nuestra lista con el número de impares pedidos.
            listaImpares += [num]
            
    print(f"Has escogido los {primerosImpares} primeros números impares, que son: {listaImpares}.")      
    
    print("Vamos a calcular ahora las áreas de los cuadrados con una medida para el lado de esos números impares...")
    
    #Mediante un list(map), podemos aplicar nuestra función areaCuadrado y guardarlo en una lista.
    areaCuadradosImpares = (list(map(Lib_DavidAlcazarSanchez.areaCuadrado, listaImpares)))
    
    #Gracias a la función zip, podremos recorrer dos listas AL MISMO TIEMPO usando dos variables. Con la primera cogeremos un número
    #en orden de la lista listaImpares, y con la segunda variable cogeremos su posición equivalente en la lista areaCuadradosImpares, 
    #mostrando una frase compuesta de ambos valores en pantalla para facilitar la vista al usuario.
    for i, j in zip(listaImpares, areaCuadradosImpares):
        print (f"El área para el cuadrado de lado {i} metros es {j} m2.")
#Opcion cerrar.
if opcion == 0:
    print ("¡Hasta luego! :)")