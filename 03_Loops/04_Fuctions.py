#Bloques de codigo reutilizables y organizados
#Funciones: def nombre_funcion(parametros):

"""definir una funcion

def nombre_de_la_funcion(parametro1, parametro2,....):
    #bloque de codigo
    #return valor_de_retorno #opcional
"""
print ("-----------------------------------------------------")
#funcion para imprimir algo en consola
print ("\nFuncion para imprimir algo en consola")
def imprimir_mensaje():
    print ("Hola desde una funcion")
imprimir_mensaje() #llamada a la funcion

print ("-----------------------------------------------------")
#funcion con parametros
print ("\nFuncion con parametros")

def saludar (nombre):
    print (f"Hola {nombre}, bienvenido a Python")
saludar("Juan") #llamada a la funcion con parametro

#el parametro es lo que acepta la funcion
print ("-----------------------------------------------------")
#funcion con mas parametros
print ("\nFuncion con mas parametros")

def sumar (a, b):
    resultado = a+b
    return resultado #retorna el valor de resultado

resultado = sumar (5, 10) #llamada a la funcion con parametros
print (f"El resultado de la suma es: {resultado}")
print ("-----------------------------------------------------")
#Documentar una funcion
print ("\nDocumentar una funcion")

def restar (a, b):
    """ Esta funcion resta dos numeros y devuelve el resultado """
    return a-b    
print (restar.__doc__) #muestra la documentacion de la funcion
resultado = restar (10, 5) #llamada a la funcion con parametros
print (f"El resultado de la resta es: {resultado}")

help(restar) #muestra la documentacion de la funcion

print ("-----------------------------------------------------")
#parametros por defecto
print ("\nParametros por defecto")
def multiplicar (a, b=2): #b tiene un valor por defecto
    return a*b
resultado = multiplicar (5) #llamada a la funcion con un parametro
print (f"El resultado de la multiplicacion es: {resultado}")
resultado = multiplicar (5, 3) #llamada a la funcion con dos parametros
print (f"El resultado de la multiplicacion es: {resultado}")
print ("-----------------------------------------------------")
#Argumentos por posicion
print ("\nArgumentos por posicion") 
def describir_persona (nombre, edad, ciudad):
    print (f"{nombre} tiene {edad} años y vive en {ciudad}")
describir_persona ("Ana", 30, "Madrid") #llamada a la funcion con argumentos por posicion

#parametros son posicionales
print ("-----------------------------------------------------")
#argumentos por clave
#parametros nombrados
print ("\nParametros nombrados")
print ("\nArgumentos por clave")

describir_persona (ciudad="Barcelona", nombre="Luis", edad=25) #llamada a la funcion con argumentos por clave
print ("-----------------------------------------------------")
#argumentos de longitud variable (*args)
print ("\nArgumentos de longitud variable (*args)")
def sumar_numeros (*args): #*args es una tupla de argumentos
    suma = 0
    for num in args:
        suma += num
    return suma
print (sumar_numeros (1, 2, 3, 4, 5)) #llamada a la funcion con varios argumentos

print ("-----------------------------------------------------")
#Argumentos de clave-valor de longitud variable (**kwargs)
print ("\nArgumentos de clave-valor de longitud variable (**kwargs)")

def mostrar_info (**kwargs): #**kwargs es un diccionario de argumentos
    for clave, valor in kwargs.items():
        print (f"{clave}: {valor}")
mostrar_info (nombre="Marta", edad=28, ciudad="Valencia") #llamada a la funcion con varios argumentos clave-valor
mostrar_info (profesion="Ingeniera", empresa="TechCorp") #llamada a la funcion con varios argumentos clave-valor
mostrar_info (nombre="Carlos", hobby="Fotografia", pais="Mexico") #llamada a la funcion con varios argumentos clave-valor

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

print ("-----------------------------------------------------")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
def imprimir_numeros_1_a_10():
    for num in range (1,11):
        print (num)
imprimir_numeros_1_a_10() #llamada a la funcion con valores por defecto

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
def imprimir_numeros_impares():
    for num in range (1,20,2):
        print (num)
imprimir_numeros_impares() #llamada a la funcion con valores por defecto
# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
def imprimir_multiplos_de_5():
    for num in range (5,51,5):
        print (num)
imprimir_multiplos_de_5() #llamada a la funcion con valores por defecto
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
def imprimir_numeros_inverso():
    for num in range (10,0,-1):
        print (num)
imprimir_numeros_inverso() #llamada a la funcion con valores por defecto
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
def suma_numeros_1_a_100():
    suma = sum(range(1,101)) #sum() suma todos los elementos de un iterable
    print (f"la suma es: {suma}")
suma_numeros_1_a_100() #llamada a la funcion con valores por defecto
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
def tabla_multiplicar (numero):
    for i in range (1,11):
        print (f"{numero} x {i} = {numero*i}")
    
tabla_multiplicar(numero) #llamada a la funcion con parametro

