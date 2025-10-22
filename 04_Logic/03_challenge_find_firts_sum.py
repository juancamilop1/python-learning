"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

# def find_first_sum(nums, goal):
#     num_map = {}  # Diccionario para almacenar números y sus índices
#     for index, num in enumerate(nums): #enumerate() devuelve el índice y el valor del elemento en cada iteración
#         complement = goal - num #el numero que falta para llegar al goal
#         if complement in num_map: #si el numero que falta para llegar al goal esta en el diccionario
#             return [num_map[complement], index] #retorna los indices del numero que falta y el indice del numero actual
#         num_map[num] = index #si no esta en el diccionario, agrega el numero actual y su indice
#     return None  # Si no se encuentra ninguna combinación
# print(find_first_sum([2, 5, 6, 2], 8))  # Output: [2, 3]

def find_first_sum(nums, goal):
    seen = {}  # Diccionario para almacenar números y sus índices
    for index, num in enumerate(nums):
        perdido = goal - num
        if perdido in seen:
            return [print(f"el numero perdido es {seen[perdido]} y su indice es {index}")] # si el numero que falta para llegar al goal esta en los vistos, retorna los indices
        seen[num] = index # guardar numero actual al los vistos si no se ha encontrado la pareja
    return None  # Si no se encuentra ninguna combinación
nums = [4, 5, 6, 2]
goal = 8            
print (find_first_sum(nums, goal)) 