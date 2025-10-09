"""
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros 
(es decir, la suma de todos los números pares en la lista).
"""

def contar_huevos_dinosaurios(egg_list)->int:
    """
    Esta función recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los de número par son de carnívoros. Devuelve un número con la suma de todos los huevos de carnívoros.
    """
    total_huevos_carnivoros = sum (huevos for huevos in egg_list if huevos % 2==0) #suma solo los numeros pares
    return total_huevos_carnivoros

egg_list = [5, 10, 15, 20, 25, 30]
print (f"La suma total de huevos de dinosaurios carnívoros es: {contar_huevos_dinosaurios(egg_list)}") #La suma total de huevos de dinosaurios carnívoros es: 60