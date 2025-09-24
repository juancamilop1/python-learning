#valores logicos: true (verdadero) y false (falso)
#fundamental para el control de flujo
#se usan en las estructuras condicionales y bucles

#importar modulos
import os 
os.system("clear") #limpiar pantalla
print ("\nValores Booleanos")
print (True)
print (False)

#operadores de comparacion
print ("\nOperadores de Comparacion")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print ("\nComparacion de cadenas")
print('"apple" == "apple":', "apple" == "apple")  # True
print('"apple" != "banana":', "apple" != "banana") # True
print('"apple" < "banana":', "apple" < "banana")   # True (orden lexicográfico)

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)    

#tabla de la verdad (referencia)
print("\nTabla de la verdad:")
print("A\tB\tA and B")
print("true\ttrue\t", True and True)
print("true\tfalse\t", True and False)
print("false\ttrue\t", False and True)
print("false\tfalse\t", False and False)
print("\nA\tB\tA or B")
print("true\ttrue\t", True or True)
print("true\tfalse\t", True or False)
print("false\ttrue\t", False or True)
print("false\tfalse\t", False or False)