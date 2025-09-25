def climbingLeaderboard(ranked, player):
    #Se convierte a set para quitar duplicados y luego a lista para poder ordenarla
    ranked = sorted(set(ranked), reverse=True) #Puntajes unicos en forma descendente
    resultado = [] # aqui se almacenan los resultados
    i= len(ranked)-1 # se iniciara desde la ultima posicion de ranked
    #se recorre cada puntaje del jugador
    for p in player:
        # se comprueba que el que no se acceda a posiciones negativas y que el puntaje del jugador sea mayor o igual al puntaje en ranked y lo guarda en i
        while i>= 0 and p >= ranked[i]:
            i-=1
            # si el puntaje del jugador es menor que el puntaje en ranked, se sale del while y se guarda la posicion i+2 en resultado
        resultado.append(i+2)
    return resultado # se retorna la lista con los resultados

