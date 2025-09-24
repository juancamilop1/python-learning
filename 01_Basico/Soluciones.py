
print("Soluciones de los ejercicios")
print("--------------")
print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
print("Juan","Bogota", sep="-")

print("--------------")
print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")
print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")
Cadena = "12345"
Entero = int (Cadena)
Flotante = float (Cadena)
float2 = 3.99
Entero2 = int (float2)
print(f"Esta es la cadena original: {Cadena}")
print(f"Esta es la cadena convertida a entero: {Entero}")
print(f"Esta es la cadena convertida a flotante: {Flotante}")
print(f"Esta es el flotante original: {float2}")
print(f"Esta es el flotante convertido a entero: {Entero2}")
print("Al convertir un float a entero, se elimina la parte decimal (se trunca).")

print("--------------")
print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
Nombre: str = "Juan"
Edad: int = 30
Altura: float = 1.80
print(f"Hola! Me llamo {Nombre} y tengo {Edad} años, mido {Altura} metros")

print("--------------")
print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
import math
PI = math.pi
print(f"El valor de PI es: {PI}")
Redondeado = round(PI)
print(f"El valor de PI redondeado es: {Redondeado/2}")
