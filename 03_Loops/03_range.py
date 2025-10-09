#permite crear una secuencia de numeros

print ("\nRange():")

nums = range(5) #0, 1, 2, 3, 4, no crea una lista, crea un objeto range
print (nums) #range(0, 5)

nums = range(2, 5) #2, 3, 4
print (nums) #range(2, 5)

nums = range(10)
#generado una secuancia de numeros del 0 a 9
for num in nums:
    print (num)
print ("-----------------------------------------------------")
#range inicio y fin
print ("range inicio y fin")
nums = range(2, 10) #2, 3, 4,
for num in nums:
    print (num)
    
print ("-----------------------------------------------------")

#range con paso, range(inicio, fin, paso)
print ("range con paso")
nums = range(2, 10, 2) #2, 4, 6,
for num in nums:
    print (num)

print ("-----------------------------------------------------")

#range con paso negativo
print ("range con paso negativo")
nums = range(-10, 2)#-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1
for num in nums:
    print (num)
print ("-----------------------------------------------------")
#sin crear variable
print ("sin crear variable")
for num in range(5, 0, -1): #5, 4, 3, 2, 1
    print (num)
    
print ("-----------------------------------------------------")
#range con lista
print ("range con lista")
nums = range(10)
lista_nums = list(nums) #convierte el objeto range en una lista
print (type(lista_nums)) #<class 'list'>
print (lista_nums) #[0, 1, 2, 3, 4 y asi hasta 9]

print ("-----------------------------------------------------")

# hacer cuantas veces uno quiera algo
# print ("hacer cuantas veces uno quiera algo")
# veces = int(input("Cuantas veces quieres que se imprima 'Hola Mundo': "))
# for _ in range (veces): #el _ se usa cuando no se necesita usar la variable
#     print ("Hola Mundo")
    
print ("-----------------------------------------------------")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for num in range (1,11):
    print (num)
# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for num in range (1,20,2):
    print (num)
# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for num in range (5,51,5):
    print (num)
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for num in range (10,0,-1):
    print (num)
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = sum(range(1,101)) #sum() suma todos los elementos de un iterable
print (f"la suma es: {suma}")
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range (1,11):
    print (f"{numero} x {i} = {numero*i}")