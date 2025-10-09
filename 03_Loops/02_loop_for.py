#permite ejecutar un bloque de codiga mientras itera un iterable o una lista
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nBucles For")

#iterar una lista
lista = [10, 20, 30, 40, 50]

for elemento in lista:
    print (elemento)
    
print  ("-----------------------------------------------------")
#iterar sobre cualquier cosa iterable
cadena = "Hola Mundo"
for letra in cadena:
    print (letra)
    # if letra == "u":
    #     print ("encontre la letra u")
    #     break #rompe el bucle
    # print ("sigue")
print  ("-----------------------------------------------------")
#iterar un rango de numeros
numero = 12143
for digito in str(numero):
    print (digito)

print  ("-----------------------------------------------------")
#enumerate: obtener indice y valor
print("\nEnumerate: obtener indice y valor")
listaropa = ["camisa", "pantalon", "zapatos"]

for index, prenda in enumerate(listaropa):
    print (f"En el indice {index} esta la prenda: {prenda}")
    
print  ("-----------------------------------------------------")
#bucles anidados
print("\nBucles anidados")
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
for letras in letras:
    for numero in numeros:
        print (f"{letras}-{numero}")
print  ("-----------------------------------------------------")
#uso del brak and continue
print("\nUso del break and continue")

animales = ["perro", "gato", "pez", "loro", "tortuga"]

print ("\nContinue\n") 
for index,animal in enumerate(animales):
    if animal == "loro": continue #salta a la siguiente iteracion
    print (animal)
    
print ("\nBreak\n") 
for index,animal in enumerate(animales):
    if animal == "pez":
        print (f"el {animal} se encontro en el indice {index}, entonces rompo el bucle")
        break #rompe el bucle
    print (animal)

print  ("-----------------------------------------------------")

#comprension de listas (List Comprehension)
print("\nComprension de listas (List Comprehension)")
animales= ["perro", "gato", "pez", "loro", "tortuga"]
animales_mayusculas = [animal.upper() for animal in animales] #convierte a mayusculas cada elemento de la lista
print (animales_mayusculas)

#compresion de listas con if 
print("\nComprension de listas con if")
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0] #filtra los numeros pares
print (pares)

print  ("-----------------------------------------------------")
###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
print ("solucion:")
for num in range(2,22,2):
    print (num)
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
cantidad = len(numeros)
for num in numeros:
    suma = sum(numeros)
media = suma / cantidad
print (f"media de los numeros: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20] 
maximo = 0
for num in numeros:
    if num > maximo:
        maximo = num
        print (maximo)
print (f"el numero maximo es: {maximo}")
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_mas_5 = [palabra for palabra in palabras if len(palabra) > 5] #list comprehension
print (palabras_mas_5)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower() #convierte a minusculas
contador = 0
for palabra in palabras:
    if palabra.lower().startswith(letra): #convierte a minusculas y verifica si empieza con la letra
        contador += 1 #incrementa el contador
print (f"Hay {contador} palabras que empiezan con la letra '{letra}'")