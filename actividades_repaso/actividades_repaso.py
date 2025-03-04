#ACTIVIDAD RAPASO NUMERO 1
"""
#asignacion y concatenacion de varibles
mensaje = "esto"
mensaje += ""
mensaje += "es"
mensaje += ""
mensaje += " una"
mensaje += ""
mensaje += " suma"
print (mensaje)
#CONCATENACION
numero ="2"
numero2 = "2"
resultado = int(numero) + int(numero2)
print("la suma es: " + str(resultado))
"""
#-------------------------------------------------------------
"""
# extraccion, busqueda, comparacion 
mensaje = "esto"
mensaje += ""
mensaje += "es"
mensaje += ""
mensaje += " mi"
mensaje += ""
mensaje += "casa"
print (mensaje)
buscar_subcadena= mensaje.find("casa")
print(buscar_subcadena)
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
#COMPARACION TRUE
mensaje1= "esta es mi casa"
mensaje2= "esta es mi casa"
print (mensaje1==mensaje2)
#COMPARACION FALSE 
mensaje3= "esta es mi cuarto"
mensaje4= "esta es mi cocina"
print (mensaje3==mensaje4)"""
#----------------------------------------------------------------
"""hacer una aplicación en la cual me muestre una suma, resta en el siguiente orden y se tiene que comentar todo 

los datos de las suma se escribirán en string  y esto se pasaran a int, esto se tiene que mostrar en pantalla

para la resta se usara la asignación para mostrar en pantalla el texto 

EJEMPLO
 
se tiene que mostrar en pantalla con asignación el siguiente texto "esto es una resta"
Se tiene que hacer dos textos diferentes (dos variables), uno explicando a un cliente como usar una licuadora y otro explicando como usar una plancha, del primer texto se tiene que extraer de la primera silaba a la novena silaba y del segundo tiene que sacarla de la tercera silaba a la octava silaba 

y buscar las palabras licuadora y plancha, tambien compararlos entre si, todo mostrandolo en pantalla y comentandolo """

#definir 2 variables con string
numero1 = "5"
numero2 = "2"
#cambiarlas a int
numero1 = int(numero1)
numero2 = int(numero2)
#Realizamos la suma de los 2 numeros
resultado_suma = numero1 + numero2
#mostramos el resultado en pantalla
print("El resultado de la suma es: " + str(resultado_suma))
 #definimos el mensaje que aparece con asignacion
mensaje_resta = "Esto"
mensaje_resta += " "
mensaje_resta += "es"
mensaje_resta += " "
mensaje_resta += "una"
mensaje_resta += " "
mensaje_resta += "Resta: "
#concatene el mensaje con la resta y converti de int a string 
print(mensaje_resta + str(numero1 - numero2))
#Definir 2 textos explicativos
mensaje_licuadora1 = "para poder usar una licuadora primero conectamos el cable para que la licuadora tenga energia coloque el ingrediente y oprima el boton para iniciar"
mensaje_plancha = "en la plancha asegure tenerle agua si es de vapor y conectarla a la corriente"
#Extraemos segun lo que necesite el cliente
print (mensaje_licuadora1  [1:9])
print (mensaje_plancha  [3:8])
#mostrar en el terminal la busqueda de la palabra licuadora y plancha
print (mensaje_licuadora1.find("licuadora"))
print (mensaje_plancha.find("plancha"))
#comparar los mensajes de true o false
print (mensaje_licuadora1 == mensaje_plancha)
