
#*PARTE 1: PALABRAS RESERVADAS 
"""son identificadores para uso exclusivo del lenguaje de programacion, que 
no pueden ser utilizadas para nombrar variables, 
metodos, objetos o cualquier elemento dentro de nuestro codigo 

PALABRAS RESERVADAS:
and, as, assert, break, class, continue, 
def, el, elif, else, except, finally, 
for, from, global, if, import, in, 
is, lambda, not, or, pass, raise, return, 
try, while, with, yield
"""
#*PARTE 2: OPERADORES ARITMETICOS

"""son utilizados para realizar operaciones entre variables y valores

OPERADORES ARITMETICOS:
+ (SUMA), - (RESTA), * (MULTIPLICACION), / (DIVISION), // (DIVISION ENTERA), % (MODULO), ** (EXPONENTE)
#!------------------------------------------------------------------------------------------------------------
SUMA: es la reunion de dos o mas conjuntos llamados "sumandos" en un conjunto llamado "suma total"

EJEMPLO:

numero_uno=5
numero_dos=2
resultado= numero_uno + numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la suma es "+ str(resultado))

#* RESULTADO
el resultado de la suma es 7
#!------------------------------------------------------------------------------------------------------------
RESTA: es la operacion contraria a la suma y tambien recibe el nombre de sustraccion. La cual consiste en extraer o quitar de un numero mayor a otro menor 

EJEMPLO:

numero_uno=5
numero_dos=2
resultado= numero_uno - numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la resta es "+ str(resultado))

#* RESULTADO
el resultado de la resta es 3
#!------------------------------------------------------------------------------------------------------------
MULTIPLICACION: es la operacion que consiste en hallar el resultado de sumar un numero tantas veces como indique 

EJEMPLO:

numero_uno=5
numero_dos=2
resultado= numero_uno * numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la multipliacion es "+ str(resultado))

#* RESULTADO
el resultado de la multiplicacion es 10
#!------------------------------------------------------------------------------------------------------------
EXPONENTE O POTENCIA: es la operacion matecartica mediante la cual multiplicamos  un numero por si mismo las veces que nos indique el exponente 

EJEMPLO:

numero_uno=5
exponente=2
#*EL RESULTADO DE UN NUMERO A LA POTENCIA ES UN NUMERO ENTERO
resultado= numero_uno ** exponente
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la potencia es "+ str(resultado))

#* RESULTADO
el resultado de la potencia es 25
#!------------------------------------------------------------------------------------------------------------
DIVISION: es una operacion matematica que consiste  en averiguar cuantas veces un numero esta contenido en otro 

EJEMPLO:

numero_uno=6
numero_dos=2
resultado= numero_uno / numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la division es "+ str(resultado))

#* RESULTADO
el resultado de la division es 3.0
#!------------------------------------------------------------------------------------------------------------
MODULO O RESTO: es la cantidad que sobra despues de efectuar una division, es decir, es el valor que se obtiene cuadno un numero no puede ser dividido exactamente por otro 

EJEMPLO:

numero_uno=5
numero_dos=2
resultado= numero_uno % numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado del modulo es "+ str(resultado))

#* RESULTADO
el resultado del modulo es 1
#!------------------------------------------------------------------------------------------------------------
DIVISION ENTERA: es una operacion que consiste en obtener el valor entero de un numero, el cual resulte de una division entre dos numeros decimales o reales 

EJEMPLO:

numero_uno=6
numero_dos=2
resultado= numero_uno // numero_dos
#* YA QUE LA VARIABLE RESULTADO ESTA EN UN FORMATO NUMERICO, LA CONVERTIMOS EN STRING PARA IMPRIMIRLA
print ("el resultado de la division entera es "+ str(resultado))

#* RESULTADO
el resultado de la division entera es 3
"""
#*PARTE 3: TIPOS DE DATOS
"""
Es un atributo de los datos que indica a la computadora y al programador, sobre la clase de datos que se va a manejar

TIPOS DE DATOS:

- Enteros y Largos: Los enteros son aquellos que no tienen decimalos, pueden ser tanto positivos como negativos y se pueden representar  mendianto el tipo int o el tipo long
- Flotantes: Son los que tienen decimales y se representa como float 
- Complejos: Son aquellos que tienen una parte real y una parte imaginaria y se representa como complex 
- CADENA: es una secuencia de caracteres que se representa encerrado el texto entre comillas 
- Booleanos: solo tener dos tipos de valores True o False, estos se usan principalmente para lo que son condicionales y bucles, se representa mediante el tipo bool
"""
#!------------------------------------------------------------------------------------------------------------
#* EJERCICIO DE LA TERCERA PARTE
#tipo de dato entero o largo

numero_entero=10
#imprimimos el numero y con (type) su tipo de dato
#la coma puede separar todo lo que son valores numericos, si se quiere concatenar un string, seria con un (+)
print (numero_entero,type(numero_entero))
#resultado 10 <class 'int'>
#*****************************************************************
#tipo de dato flotante

numero_flotante=10.5
#imprimimos el numero y con (type) su tipo de dato
print (numero_flotante,type(numero_flotante))
#resultado 10.5 <class 'float'>
#*****************************************************************
#tipo de dato numero complejo

numero_complejo=3j+2j
#imprimimos el numero y con (type) su tipo de dato
print (numero_complejo,type(numero_complejo))
#resultado (3+2j) <class 'complex'>
#*****************************************************************
#tipo de dato string

cadena="Hola, mundo!"

#imprimimos el numero y con (type) su tipo de dato
print (cadena,type(cadena))
# resultado Hola, mundo! <class 'str'>
#*****************************************************************
#tipo de dato booleano
#dos signos de igual es una comparacion y un solo signo de igual es una asignacion
verdadero_falso= 3 == 3
#imprimimos el numero y con (type) su tipo de dato
print (verdadero_falso,type(verdadero_falso))
# resultado True <class 'bool'>