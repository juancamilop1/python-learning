#ACTIVIDAD RAPASO NUMERO 1
#asignacion y concatenacion de varibles
mensaje = "esto"
mensaje += ""
mensaje += "es"
mensaje += ""
mensaje += " una"
mensaje += ""
mensaje += " suma"
print (mensaje)
#CONCATENACION
numero ="2"
numero2 = "2"
resultado = int(numero) + int(numero2)
print("la suma es: " + str(resultado))
#-------------------------------------------------------------
# extraccion, busqueda, comparacion 
mensaje = "esto"
mensaje += ""
mensaje += "es"
mensaje += ""
mensaje += " mi"
mensaje += ""
mensaje += "casa"
print (mensaje)
buscar_subcadena= mensaje.find("casa")
print(buscar_subcadena)
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
#COMPARACION TRUE
mensaje1= "esta es mi casa"
mensaje2= "esta es mi casa"
print (mensaje1==mensaje2)
#COMPARACION FALSE 
mensaje3= "esta es mi cuarto"
mensaje4= "esta es mi cocina"
print (mensaje3==mensaje4)