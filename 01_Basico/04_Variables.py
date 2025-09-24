#Las variables sirven para almacenar datos en memoria
#python es un lenguaje de tipado dinamico, no es necesario declarar el tipo de variable
#Asinacion de variables
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
print ("\nAsignacion de variables:")
# mi_variable = 4
# mi_nombre = "juan"
# print (mi_variable)
# print (mi_nombre)

# Edad = 30
# print (Edad)
# Edad = 31 #se puede cambiar el valor de la variable
# print (Edad)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Las variables pueden cambiar de tipo
print ("\nVariables pueden cambiar de tipo:")
# name = "Ernesto"
# print (type(name))
# name = 4
# print (type(name))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#tipado fuerte: no se pueden hacer operaciones entre tipos diferentes
print ("\nTipado fuerte:")
# prueba_int = 4
# prueba_str = "Hola"
# # (f) para formatear y solo leer lo que esta dentro de las llaves {}
# # print (prueba_int + int(prueba_str)) #error
# # print (str(prueba_int) + prueba_str) #error
# print (f"El valor de la variable prueba_int es: {prueba_int} y el valor de la variable prueba_str es: {prueba_str}")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#operaciones con formateo
print ("\nOperaciones con formateo:")
# numero_uno = 4
# numero_dos = 6
# prueba_str = "Hola"
# print (f"este es una prueba con la variable str: {prueba_str} y la suma de las variables numero_uno: {numero_uno} y numero_dos: {numero_dos} es igual a:  {numero_uno + numero_dos}")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Tipo de casos 
print ("\nOtros tipos de casos:")
# numero_uno = 4
# numero_dos = 6
# resultado = numero_uno + numero_dos
# print (f"El resultado de la suma es: {resultado}")
# print ("El resultado de la suma es: " + str(resultado)) #concatenacion
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Constante
#python no tiene constantes, pero se acostumbra a usar mayusculas para identificarlas
print ("\nConstantes:")
# MI_CONSTANTE = 3.1416 #Se utiliza uppercase para identificar que es una constante
# print (MI_CONSTANTE)
# MI_CONSTANTE = 2.7183 #No es recomendable cambiar el valor de una constante
# print (MI_CONSTANTE)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#No se pueden usar palabras reservadas como nombres de variables
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Anotacion de variables
#Se llama TypeAnnotations
#No es obligatorio, pero ayuda a entender el tipo de dato que se espera en la variable
print ("\nAnotacion de variables:")
# mi_variable: int = 4
# mi_nombre: str = "juan"
# print (mi_variable)
# print (mi_nombre)
# #Si lo volvemos estricto en la configuracion no se podran cambiar el valor de la variable
# # mi_variable = "Hola" #error
#si volvemos estatico una variable anterior ahora, va a fallar antes
