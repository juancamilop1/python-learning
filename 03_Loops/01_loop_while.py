#Permiten ejecitar un bloque de codigo mientras se cumpla una condicion
#para romper un bucle se usa break
#para saltar a la siguiente iteracion se usa continue
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
os.system("clear")  # limpiar pantalla
print("\nBucles While")
# contador = 0

# while contador <= 5:
#     print (contador)
#     contador += 1  # contador = contador + 1
    
print("\nBucle infinito con break")
# contador = 0
# while True:
#     print (contador)
#     contador += 1
#     if contador > 10:
#         break
print  ("-----------------------------------------------------")
# while contador <100:
#     contador += 1
#     print (contador)
#     if contador % 5 == 0:
#         print ("numero multiplo de 5:", contador)
#         break
print  ("-----------------------------------------------------")
#continue salta a la siguiente iteracion
print("\nContinue salta a la siguiente iteracion")
print ("bucle con continue")
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador %2 == 0: 
#         continue#si el numero es par, salta a la siguiente iteracion
#     print (contador)#imprime solo numeros impares
print  ("-----------------------------------------------------")

#else ejecuta cuando el bucle termina normalmente (sin break)
print("\nElse ejecuta cuando el bucle termina normalmente (sin break)")
# contador = 0
# while contador < 5:
#     print (contador)
#     contador += 1
# else: 
#     print ("El bucle ha terminado normalmente")

#pedir al usuario dentro del bucle que ingrese un numero
print("\nPedir al usuario dentro del bucle que ingrese un numero")

# numero = -1
# while numero < 0:
#     numero = int(input("Ingresa un numero positivo: "))
#     if numero < 0:
#         print ("El numero es negativo, intenta de nuevo")
# else:
#     print (f"El numero ingresado es: {numero}")
    
#mismo ejercicio con control de errores
print("\nMismo ejercicio con control de errores")
# numero = -1
# while numero < 0:
#     try:
#         numero = int(input("Ingresa un numero positivo: "))
#         if numero < 0:
#             print ("El numero es negativo, intenta de nuevo")
#     except ValueError:
#         print ("Eso no es un numero, intenta de nuevo")
# else:
#     print (f"El numero ingresado es: {numero}")
    


###
# EJERCICIOS (while)
###
print ("\nEjercicios (while)")
# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador =10
while contador>=1:
    print (contador)
    contador -=1
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
suma =0
lista = []
i=0
while suma<=20:
    suma +=1
    if suma%2==0:
        lista.insert(i,suma)
        i+=1
else:
    print (f"esto es la suma: {sum(lista)}") #esto es la suma: 110 , guarda en una lista los numeros pares y luego los suma

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

while True:
    try: 
        n = int(input("Introduce un número entero positivo para calcular su factorial: "))
        if n < 0:
            print ("El numero es negativo, intenta de nuevo")
            continue
        multiplicado=1
        numero= n
        while n>0:
                multiplicado *= n
                n -=1
        else:
            print (f"El factorial de {numero} es: {multiplicado}")
        break
    except ValueError:
        print ("Eso no es un numero, intenta de nuevo")



# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
contraseña = ""
while True: 
        contraseña = input("Introduce una contraseña (mínimo 8 caracteres): ")
        if len(contraseña) >= 8:
            print ("Contraseña válida")
            break     
        else:
            print ("Contraseña inválida, intenta de nuevo")
# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
i=1

while True:
    try: 
        num = int(input("intrudce un numero del que quieras saber la tabla de multiplicar: "))
        while i<=10:
            print (f"{num} * {i} = {num*i}")
            i+=1
        break
    except ValueError:
        print ("Eso no es un numero, intenta de nuevo")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
verificacion = 2
while True:
    try: 
        num = int(input("intrudce un numero: "))
        if num <=1:
            print ("El numero 1 y 0 no es primo, intenta de nuevo")
            continue
        while verificacion <= num: #verifica todos los numeros desde el 2 hasta el numero ingresado
            divisor =2 #un numero es primo si no es divisible por ningun numero entre 2 y la raiz cuadrada del mismo
            while divisor * divisor<=verificacion: #mientras el cuadrado del divisor sea menor o igual que el numero a verificar
                if verificacion % divisor ==0: #no es primo
                    break
                divisor +=1
            else:
                print (verificacion, end=" ") #es primo
            verificacion +=1
        break
    except ValueError:
        print ("Eso no es un numero, intenta de nuevo")
