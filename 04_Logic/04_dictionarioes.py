#los diccionarios son colecciones de clave-valor
#sirven para almacenar datos relacionados


#ejemplo tipico de diccionario 
print ("Ejemplo tipico de diccionario")

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(persona["edad"]) #accede al valor de la clave edad
print(persona["ciudad"])

print ("-----------------------------------------------------")

#cambiar valor al acceder 
print ("\nCambiar valor al acceder")
persona["edad"] = 31 #cambia el valor de la clave edad
print(persona["edad"])


#eliminar una propiedad 
print ("\nEliminar una propiedad")
del persona["ciudad"] #elimina la clave ciudad
print(persona)

#pop para eliminar y obtener el valor
print ("\nPop para eliminar y obtener el valor")

edad = persona.pop("edad") #elimina la clave edad y devuelve su valor
print(f"edad: {edad}") 
print(persona)

#sobreescribir un diccionario con otro diccionario
print ("\nSobreescribir un diccionario con otro diccionario")

a = { "name": "Alice", "age": 25 }
b = { "age": 30, "city": "New York" }
a.update(b) #sobreescribe a con b
print(a) # {'name': 'Alice', 'age': 30, 'city':


#comprobar si existe una propiedad 
print ("\nComprobar si existe una propiedad ")
print ("name" in persona) # False
print ("nombre" in persona) # True

p = { "nombre" : "Ana", "edad": 28, "ciudad": "Barcelona" }

persona.update(p) #actualiza persona con p
#obtener todas las claves
print ("\nObtener todas las claves")
print(persona.keys()) #dict_keys(['nombre'])

#obtener todos los valores
print ("\nObtener todos los valores")
print(persona.values()) #dict_values(['Juan'])

#obtener todas las claves y valores
print ("\nObtener todas las claves y valores")
print(persona.items()) #dict_items([('nombre', 'Juan')])


for clave, valor in persona.items(): #itera sobre las claves y valores
    print(f"{clave}: {valor}")