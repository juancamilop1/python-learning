#metodos mas importantes de las listas

import os 
os.system("clear") #limpiar pantalla
print ("\nMetodos mas importantes de las listas")

lista = [1, 2, 3, 4, 5]
print ("Lista inicial:", lista)
#agregar elementos a una lista
print ("\nagregar elementos a una lista")
# #append: agrega un elemento al final de la lista
print ("\nappend: agrega un elemento al final de la lista")
# lista.append(6)
# print ("Lista despues de append:", lista)
# #extend: agrega multiples elementos al final de la lista
print ("\nextend: agrega multiples elementos al final de la lista")
# lista.extend([7, 8, 9])
# print ("Lista despues de extend:", lista)
# #insert: agrega un elemento en una posicion especifica
print ("\ninsert: agrega un elemento en una posicion especifica")
# lista.insert(0, 0) #posicion 0, valor 0
# print ("Lista despues de insert:", lista)

#eliminar elementos de una lista
print ("\neliminar elementos de una lista")
#remove: elimina la primera ocurrencia de un valor especifico
print ("\nremove: elimina la primera ocurrencia de un valor especifico")
# lista.remove(3)
# print ("Lista despues de remove:", lista)

#pop: elimina y devuelve el elemento en una posicion especifica
print ("\npop: elimina y devuelve el elemento en una posicion especifica")
# elemento = lista.pop(2) #posicion 2
# print ("Elemento eliminado con pop:", elemento)
# print ("Lista despues de pop:", lista)

#index: devuelve el indice de la primera ocurrencia de un valor especifico
print ("\nindex: devuelve el indice de la primera ocurrencia de un valor especifico")
# indice = lista.index(4)
# print ("Indice del valor 4:", indice)
#Si el valor no existe, lanza un error
#indice = lista.index(10) #ValueError: 10 is not in list    

#Eliminar rango de elementos
print ("\nEliminar rango de elementos")
# del lista[1:3] #elimina elementos desde el indice 1 hasta el 2
# print ("Lista despues de eliminar rango de elementos:", lista)

#ordenar una lista
print ("\nordenar una lista")
#sort: ordena la lista en orden ascendente
print ("\nsort: ordena la lista en orden ascendente")
# lista.sort()
# print ("Lista despues de sort:", lista)

#sort con parametro reverse=True: ordena la lista en orden descendente
print ("\nsort con parametro reverse=True: ordena la lista en orden descendente")
# lista.sort(reverse=True)
# print ("Lista despues de sort con reverse=True:", lista)

#ordenar lista creando una nueva lista
print ("\nordenar lista creando una nueva lista")
# lista_ordenada = sorted(lista)
# print ("Lista original:", lista)
# print ("Nueva lista ordenada con sorted():", lista_ordenada)

#ordenar cadena de texto (minusculas)
print ("\nordenar cadena de texto (minusculas)")
lista_cadena = ["banana", "apple", "cherry", "date"]
# lista_cadena.sort()
# print ("Lista de cadenas ordenada:", lista_cadena)
#ordenar cadena de texto (mayusculas y minusculas)
print ("\nordenar cadena de texto (mayusculas y minusculas)")
lista_cadena_mayus = ["banana", "Apple", "cherry", "date"]
# lista_cadena_mayus.sort() #mayusculas primero
# print ("Lista de cadenas con mayusculas ordenada:", lista_cadena_mayus)
#ordenar cadena de texto ignorando mayusculas y minusculas
print ("\nordenar cadena de texto ignorando mayusculas y minusculas")
# lista_cadena_mayus.sort(key=str.lower)
# print ("Lista de cadenas ignorando mayusculas ordenada:", lista_cadena_mayus)

#contar cuantas veces aparece un elemento en una lista
print ("\ncontar cuantas veces aparece un elemento en una lista")
#count: cuenta cuantas veces aparece un elemento en la lista
print ("\ncount: cuenta cuantas veces aparece un elemento en la lista")
lista.append(2)
lista.append(2)
print ("Lista despues de agregar dos veces el 2:", lista)
print ("Numero de veces que aparece el 2 en la lista:",lista.count(2))

#comprobar si un elemento existe en una lista
print ("\ncomprobar si un elemento existe en una lista")
#in: devuelve True si el elemento existe en la lista, False en caso contrario
print ("\nin: devuelve True si el elemento existe en la lista, False en caso contrario")
existe = 3 in lista
print ("El 3 existe en la lista?:", existe)
no_existe = 10 in lista
print ("El 10 existe en la lista?:", no_existe)


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###
print ("\nEjercicios")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

#solucion 
print ("\nSoluciones")
print ("--------------")
print ("\nEjercicio 1: Añadir y modificar elementos")
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
lista = [1,2,3,4,5]
lista.append(6)
lista.insert(2,10)
lista[0]=0
print (lista)

print ("--------------")
print ("\nEjercicio 2: Combinar y limpiar listas")
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
num_eliminado= lista_a.pop(3)
print ("Elemento eliminado con pop:", num_eliminado)
lista_b.clear()
print ("Lista A:", lista_a)
print ("Lista B:", lista_b)

print ("--------------")

print ("\nEjercicio 3: Slicing y eliminación con del")
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
lista = [1,2,3,4,5,6,7,8,9,10]
del lista [2:5]
print (lista)

print ("--------------")
print ("\nEjercicio 4: Ordenar y contar")
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
Conteo =lista.count(2)
existe = 7 in lista
print ("Numero de veces que aparece el 2 en la lista:",Conteo)
print ("existe el 7 en la lista?:", existe)
print ("Lista ordenada:", lista)

print ("--------------")
print ("\nEjercicio 5: Copia vs. Referencia")
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
original = [1,2,3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print ("Original:", original)
print ("Copia 1:", copia_1) 
print ("Copia 2:", copia_2)
print ("Referencia:", referencia)

print ("--------------")
print ("\nEjercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.")
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
lista_cadenas = ["Manzana", "pera", "BANANA", "naranja"]
lista_cadenas.sort(key=str.lower)
print ("Lista de cadenas ordenada sin diferenciar mayusculas y minusculas:", lista_cadenas)
print ("--------------")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------- --- IGNORE ---