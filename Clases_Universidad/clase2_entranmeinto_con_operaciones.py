#calcule a con base en la siguiente formula a=p(pi)*(r)2
#se importa esta libreria para hacer operaciones matematicas

# si son iguales o no son  iguales
"""calcule base de x, si x es positivo entonces f(x)=(x-2)2+(x-4)4/2+(x-6)6/4*Z 
Y si es negativo entonces f(x)=(x+2)2+(x+4)2/2+w"""

#primero 
R=int(input("ESCRIBE R: "))
#el doble asterisco se ignifica potencia 
resultado=3.1416*(R**2)
print (resultado)
#segundo
x1=int(input("ESCRIBE EL PRIMER DIGITO: "))
x2=int(input("ESCRIBE EL SEGUNDO DIGITO: "))
if x1==x2:
    print("SON IGUALES")
else:
    print("SON DIFERENTES")

#TERCERO
X=int(input("ESCRIBE VALOR DE X:  "))

if X<0:
    W=int(input("escriba el valor de W: "))
    resultado=((X+2)*2)+(((X+4)*2)/2)+W
    print(resultado)
else:
    Z=int(input("escriba el valor de Z: "))
    resultado=((X-2)*2)+(((X-4)*4)/2)+(((X-6)*6)/4)*Z
    print(resultado)