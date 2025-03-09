import math
#*para que python escojo un numero random (esto se usa en el ejercicio numero dos)
import random
#*primer ejercicio 
#*se crea una funcion que escriba la operacion necesaria 
def calcular_x (a,b,n):
    suma=sum(((a-b)**i-3) for i in range(1,n+1))+n
    producto=1
    for i in range(2,n):
        producto*=(2+a*(i-1))
    x=suma/producto 
    #*hacemos que retorne el resultado, en este caso x
    return x
#*damos el valor para cada variable de clase int y dos float 
n=int(input("ESCRIBE EL VALOR DE N: "))
a= float (input("ESCRIBE EL VALRO DE A"))
b= float (input("ESCRIBE EL VALRO DE B"))
#*aqui retornamos la funcion anteriormente realizada 
resultado= calcular_x( a,b,n)
print ("el resultado es: ", resultado)


#*segundo ejercicio 
print ("Hola usuario adivina el numero")
#*creamos una variable que nos de un numero del 1 al 100
numero_random=random.randint(1,100)
#*hacemos que el usuario adivine el numero
numero=int(input("adivina el numero :"))
#*esto comprueba si son iguales o no, al no serr iguales se repetira la secuencias de if
while True:
    #*se puede mejorar usando el else if
    if numero<numero_random:
        print("el numero es mayor al que escogiste")
        numero=int(input("escribe otro numero :"))
    if numero>numero_random:
        print("el numero es menor al que escogiste")
        numero=int(input("escribe otro numero :"))
        #*este if funciona cuando el numero sea igual y se activa el break 
    if numero==numero_random:
        print("el numero que escogiste esta bien")
    
        #*esto termina el programa y hace que e salga del while true
        break


#*TERCER EJERCICIO
def calcular_digito_seguridad(clave,codigo):
    #*esto hace que se calcule cada digito entre clave y codigo
    suma=sum(c*k for c,k in zip(clave,codigo))
    #*que agarre el ultimo digito 
    digito_seguridad= suma%10
    return digito_seguridad
#*aqui hacemos que nos de un lista y con la funcion map hacemos que cada uno de los digitos se puedan usar 
clave=list(map(int,input("escriba los 6 digitos de la clave: ")))
codigo= list(map(int,input("escriba los 6 digitos del codigo: ")))
#*aqui validamos si estan bien los 6, la funcion (len) cuenta cada uno de ellos
if len(codigo)==6 and len(clave)==6:
    digito_seguridad=calcular_digito_seguridad(clave,codigo)
    print (f"el digito de seguridad es {digito_seguridad}")
else:
    print ("se deben ingresar los 6 digitos")
