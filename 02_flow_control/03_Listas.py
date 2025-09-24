#Secuencias mutables de elementos
#Listas, Conjuntos, Diccionarios
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creacion de listas
import os 
os.system("clear") #limpiar pantalla

print ("Creacion de listas")
# lista1 = [1, 2, 3, 4, 5] #Lista de enteros
# lista2 = ["Hola", "Mundo", "Python"] #Lista de cadenas
# lista3 = [1, "Hola", 3.14, True] #Lista mixta

# lista_vacia = [] #Lista vacia
# lista_de_listas = [[1, 2], [3, 4], [5, 6]] #Lista de listas

# matriz = [
#     [1, 2, 3,"banana"],
#     [4, 5, 6,"papaya"],
#     [7, 8, 9,"mango"]
# ] #Matriz de 3x4

# print (lista1)
# print (lista2)
# print (lista3)
# print (lista_vacia)
# print (lista_de_listas)
# print (matriz)

#acceder a elementos por indice
print ("\nAcceso a elementos por indice")
# print (lista2[0]) #Primer elemento
# print (lista2[1]) #Segundo elemento
# print (lista2[2]) #Tercer elemento
# print (lista2[-1]) #Ultimo elemento
# print (lista2[-2]) #Penultimo elemento
# print (lista2[-3]) #Antepenultimo elemento

print ("\nAcceso a elementos por indice en una matriz")
# print (matriz[0][3])#Elemento fila 0, columna 2
# print (matriz[1][3])#Elemento fila 1, columna 1
# print (matriz[2][3])#Elemento fila 2, columna 2

#Slicing (rebanado) de listas
print ("\nSlicing (rebanado) de listas")
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (lista[1:5]) #Elementos desde el indice 1 hasta el 4
# print (lista[:5])  #Elementos desde el inicio hasta el indice 4
# print (lista[5:])  #Elementos desde el indice 5 hasta el final
# print (lista[-5:]) #Ultimos 5 elementos
# print (lista[:])  #Copia de la lista completa

# print (lista[::2]) #Elementos desde el inicio hasta el final, saltando de 2 en 2
# print (lista[1::2]) #Elementos desde el indice 1 hasta el final, saltando de 2 en 2
# print (lista[::-1]) #Elementos desde el final hasta el inicio (lista invertida)
# print (lista[7:3:-1]) #Elementos desde el indice 7 hasta el 4, en orden inverso

#moodificar elementos de una lista
print ("\nModificar elementos de una lista")
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista[0] = 10
# lista[1] = 20
# lista[2] = 30
# print (lista)

#Agregar elementos a una lista
print ("\nAgregar elementos a una lista")
# lista1 = [1, 2, 3]
# #forma larga y menos eficiente
# lista1 = lista1 + [4,5,6] #Concatenacion
# print (lista1)

# #forma corta y mas eficiente
# lista1 += [7,8,9] #Concatenacion
# print (lista1)

#Recuperar la longitud de una lista
print ("\nRecuperar la longitud de una lista")
# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (len(lista)) #Longitud de la lista
###
# EJERCICIOS
###
print ("\nEjercicios")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

#Solucion De Los Ejercicios
print ("\nSoluciones de los ejercicios")
print ("--------------")
# Ejercicio 1: El mensaje secreto
print ("\nEjercicio 1: El mensaje secreto")
#Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print (mensaje[7:])#Solucion

print ("--------------")
# Ejercicio 2: Intercambio de posiciones
print ("\nEjercicio 2: Intercambio de posiciones")
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros [-1], numeros[0] #Solucion
print (numeros)

print ("--------------")
# Ejercicio 3: El sándwich de listas
print ("\nEjercicio 3: El sándwich de listas")
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich =pan+ingredientes+pan_abajo #Solucion
print (sandwich)

print ("--------------")
# Ejercicio 4: Duplicando la lista
print ("\nEjercicio 4: Duplicando la lista")
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista = [1, 2, 3]
lista2 = lista * 2 #Solucion
print (lista2)
print ("--------------")
# Ejercicio 5: Extrayendo el centro
print ("\nEjercicio 5: Extrayendo el centro")
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
lista = [10, 20, 30, 40, 50]
lista_centro = len(lista)//2#esto lee cuantos elementos tiene la lista y lo divide entre 2 para obtener el centro
print (f"El centro es: {lista[lista_centro]}")#Solucion
print ("--------------")
# Ejercicio 6: Reversa parcial
print ("\nEjercicio 6: Reversa parcial")
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista)//2
lista[:mitad] = lista[:mitad][::-1] #Solucion
print (lista)