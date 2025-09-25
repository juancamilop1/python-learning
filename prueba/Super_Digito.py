def superDigit(n,k):
    #Si la cadena tiene un solo digito automáticamente mostrara ese digito 
    if len(n) == 1:
        # Se convierte la cadena a entero y se retorna
        return int(n)
    else: #entrara aqui si la cadena tiene mas de un digito
        """convierte cada caracter de (n) en un entero y los suma entre si,
        luego se multiplica por k todo esto para simular 
        la concatenacion de n las veces de k"""
        suma = sum(int(digito) for digito in n) * k
        return superDigit(str(suma), 1) # se llama a la funcion para que este trabaje con el numero mas pequeño
    
print (superDigit("148", 3))  # Output: 3

