"""manipulacion de cadena de caracteres
es una serie de caracteres compuestas por letras, numeros, signos y simbolos, dentro de sus funciones esta la interaccion de un programa con el usuario

Existen distintas operaciones para manejar estos, los cuales son: 
#!---------------------------------------------------------------------------------------------------------------------------
-la asignacion: consiste en asignar una cadena de caracteres a otra, para lo cual es necesario utilizar el operador (+=)

EJEMPLO 

mensaje="Hola"
mensaje+="" (esto seria un espacio)
mensaje+="Ernesto"
print(mensaje)

RESULTADO

Hola_Ernesto
#!-----------------------------------------------------------------------------------------------------------------------------
-concatenacion: es una operacion que consiste en unir dos cadenas o mas, para formar una cadena de mayor tamaño para lo cuak se utiliza el operador (+)

EJEMPLO

mensaje="Hola"
espacio=""
nombre="Ernesto"
print(mensaje+espacio+nombre)

EJEMPLO CON CAMBIO DE VALOR DE VARIBLE

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos 
resultado = str (resultado)
print("El resultado de la suma es: " + resultado)

RESULTADO

El resultado de la suma es: 10
#!----------------------------------------------------------------------------------------------------------------------------------
-La busqueda: consiste en localizar dentro de una cadena, una subcadena mas pequeña a un caracter, para lo cual es neceario el metodo (find)

EJEMPLO

mensaje = "Hola Ernesto"
buscar_subcadena= mensaje.find("Ernesto")
print(buscar_subcadena)

RESULTADO

5 (se empieza a contar desde 0 a partir del primer caracter, en el 5 caracter esta ernesto)
#!.................................................................................................................................

-La extraccion: se trata de sacar fuera de una cadena, una porcion de la misma segun su posicion dentro de ello, para eso es necesario indicar la poscion a extraer [1:8]

EJEMPLO

mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

RESULTADO

ola Ern
#!-----------------------------------------------------------------------------------------------------------------------------------
-La comparacion: se utiliza para comnparar dos cadenas de caracteres, para ello se utiliza el operador (==)

EJEMPLO

mensaje1 = "Hola"
mensaje2 = "Hola"
print(mensaje1 == mensaje2)

RESULTADO

True (las cadenas son iguales)

"""