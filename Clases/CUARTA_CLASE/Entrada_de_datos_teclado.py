
#*ENTRADA DE DIFERENTES DATOS 
"""
#input hara que el usuario pueda digitar lo que quiere, hacemos que solo pueda ser un entero o lo que se prefiera, en este caso la variable entero con (int)
palabra=(input("escribe tu nombre:  "))
entero=int(input("escribe un numero entero:  "))
numero_flotante=float(input("escribe un numero flotante:  "))
numero_complejo=complex(input("escribe un numero complejo:  "))
#aqui lo que hacemos es hacer una comparacion con lo que escriba el usuario 
booleano= 3 == int(input("escribe 3 si quieres que el booleano salga true sino escribe otro para que salga false:  "))
#mostramos el resultado de cada uno
print(palabra)
print(entero)
print(numero_flotante)
print(numero_complejo)
print(booleano)
"""
#*EJERCICIO, HACER UNA MULTIPLICACION

nombre = input("Bienvenido usuario, digite su nombre para comenzar con la multipliacion: ")

print (" VAMOS A COMENZAR ") 
primer_numero=int(input("introduce el primer numero: "))

segundo_numero=int(input("introduce el segundo numero: "))
#las variables de tipo string se concatenan con un (+) y las de tipo numerico con una (,), hacemos la operacion dentro del print 
print (nombre+" el resultado es ", (primer_numero*segundo_numero))