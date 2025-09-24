#Sentencias Condicionales
#Si se cumple una condición, se ejecuta un bloque de código. Si no, se (if, else, elif)

#importar modulos
import os 
os.system("clear") #limpiar pantalla

print ("\nsentencia simple condicional")

# edad = 18
# if edad >= 18:
#     print ("Eres mayor de edad")
#     print ("Felicidades")
# else :
#     print ("Eres menor de edad")
    
print ("\nsentencia condicional con elif")

# nota = 5

# if nota >= 5:
#     print ("Superior")
# elif nota < 5 and nota >= 4:
#     print ("Alto")
# elif nota < 4 and nota >= 3:
#     print ("Basico")
# else :
#     print ("Insuficiente")

print ("\nCondiciones Multiples")
# edad = 18
# Tiene_Cedula = True

# if edad >= 18 and Tiene_Cedula:
#     print ("Eres mayor de edad y tienes cedula")
# elif edad >= 18 and not Tiene_Cedula:
#     print ("Eres mayor de edad y no tienes cedula")
# else :
#     print ("Eres menor de edad")
    
#Condicion con operador or
print ("\nCondicion con operador or")
# edad = 18
# Tiene_Cedula = False
# if edad >= 18 or Tiene_Cedula:
#     print ("Eres mayor de edad o tienes cedula")
# else :
#     print ("Eres menor de edad")
    
#Anidar condiciones
print ("\nAnidar condiciones")
# edad = 18
# Tiene_Cedula = True
# if edad >= 18:
#     if Tiene_Cedula:
#         print ("Eres mayor de edad y tienes cedula")
#     else:
#         print ("Eres mayor de edad y no tienes cedula")
# else :
#     print ("Eres menor de edad")
    
#Evaluar como booleano
print ("\nEvaluar como booleano")

# numero = 5
# if numero:  # Evalúa si 'numero' es diferente de cero
#     print ("El número es diferente de cero")
    
# numero = 0
# if numero:  # Evalúa si 'numero' es igual a cero
#     print ("El número es igual cero")
    
# nombre = ""
# if nombre:  # Evalúa si 'nombre' no está vacío  
#     print ("El nombre no está vacío")
# else:
#     print ("El nombre está vacío")
    

# numero = 3 #Asignacion
# #si no es igual dara error de sintaxis
# Comparacion_Numero = numero == 3 #Comparacion

# if Comparacion_Numero: 
#     print ("El numero es igual a 3")

#Condicion Ternarea
print ("\nCondicion ternarea")
#es una forma corta de escribir una condicion if-else
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]
# edad = 18
# mensaje = "Es mayor de edad" if edad >=18 else "es menor de edad"
# print (mensaje)

###
# EJERCICIOS
###
print ("\nEjercicios")
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#Solucion Ejercicio 1 (SOLUCIONADO)
print ("\nEjercicio 1: Determinar el mayor de dos números")
# num1 = input("Introduce el primer número: ")
# num2 = input("Introduce el segundo número: ")
# num1 = int(num1)
# num2 = int(num2)
# if num1 > num2:
#     print (f"El número {num1} es mayor que {num2}")
# elif num1 == num2:
#     print (f"Los números son iguales: {num1} = {num2}")
# else: 
#     print (f"El número {num2} es mayor que {num1}")

#Solucion Ejercicio 2 (SOLUCIONADO)
print ("\nEjercicio 2: Calculadora simple")
# num1 = input("Introduce el primer número: ")
# num2 = input("Introduce el segundo número: ")
# operacion = input("Introduce la operación (+, -, *, /): ")
# num1 = int(num1)
# num2 = int(num2)
# if operacion == "+":
#     resultado = num1 + num2
#     print (f"El resultado de la suma es: {resultado}")
# elif operacion == "-":
#     resultado = num1 - num2
#     print (f"El resultado de la resta es: {resultado}") 
# elif operacion == "*":
#     resultado = num1 * num2
#     print (f"El resultado de la multiplicación es: {resultado}")
# elif operacion == "/":
#     if num2 != 0:
#         resultado = num1 / num2
#         print (f"El resultado de la división es: {resultado}")
#     else:
#         print ("Error: División entre cero no permitida")
# else:
#     print ("Operación no válida")

#Solucion Ejercicio 3 (SOLUCIONADO)
print ("\nEjercicio 3: Año bisiesto")
# Año =  input ("intruduce un año: ")
# Año = int(Año)
# if Año %4 == 0 and Año%100 != 0 or Año%400 == 0:
#     print (f"El año {Año} es bisiesto")
# else:
#     print (f"El año {Año} no es bisiesto")

#Solucion Ejercicio 4 (SOLUCIONADO)
print ("\nEjercicio 4: Categorizar edades")
# Edad = input ("introduce tu edad:")
# Edad = int(Edad)
# if edad >=0 and Edad <=2:
#     print ("Eres un bebe")
# elif Edad>=3 and Edad <=12:
#     print ("Eres un niño")
# elif Edad>=13 and Edad <=17:
#     print ("Eres un adolescente")
# elif Edad>=18 and Edad <=64:
#     print ("Eres un adulto")
# else:
#     print ("Eres un adulto mayor")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------