
"""imprimir en pantalla"""
a=1
b=2
print (a,"------",b)
print ("fin")

"""
#-------------------------------------------------------------
"""
"""concatenar"""

s="hola mundo"
palabra2= "ciao"
resultado=s+palabra2
a=1
b=2
c=a+b
print("la concatenacion es: ", resultado)
print (s)
print (a)
print (b)
print (c)
print ("fin")
"""
#-------------------------------------------------------------
"""
"""entrada y salida"""

print ("escanear")

entrada= input("escribe lo que vas a escanear: ")

print ("mostrar lo escaneado")

"""aqui se mostrara lo que hayas escrito en el input"""

print (f"{entrada}")#
print ("fin")

"""
#-------------------------------------------------------------
"""
"""sentencias if"""
print ("escanear edad")

"""para que un if funcione tienen que ser las varibles iguales, si lo comparo con un entero se tiene que convertir en entero o si lo 
comparo con un string lo convierto en string"""

edad= int(input ("escribir edad: "))

"""lo que este mal identado no funciona"""

if edad >= 18:
    print("puede beber")
else:
    print("no puede beber")
    
print (f"su edad es: {edad}")

print ("fin")	

"""
#-------------------------------------------------------------
"""
"""Expresiones Lógicas y Operadores Lógicos"""
print ("escanear edad")
edad= int(input ("escribir edad: "))
#-----------------------------------------------------------------------------

