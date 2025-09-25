def evenForest(t_nodes, t_edges, t_from, t_to):
    # Se crea un grafo (este se usa normalmente para representar relaciones o conexiones)
    # Crear lista de adyacencia, esto nos representaria el arbol 
    ListaAdya = {i: [] for i in range(1, t_nodes + 1)}
    for i, u in enumerate(t_from): #t_from y t_to representan las aristas del arbol
        v = t_to[i] #nodo destino
        ListaAdya[u].append(v) #esto conecta a la arista u con v
        ListaAdya[v].append(u) #esto conecta a la arista v con u es un grafo no dirigido(esto sigifica que se puede ir en ambos sentidos)
    #Se usa una lista para poder modificar el valor dentro de la funcion recursiva (Recorrido)
    ParCortes = [0]
    #Esta funcion recursiva recorrera el arbol y contara los nodos en cada subarbol
    def Recorrido(nodo, Anterior):      
        tamano = 1 # empezamos contando el nodo actual
        # recorremos cada subnodo conectado al nodo actual
        for subnodo in ListaAdya[nodo]:
            # evitamos volver al nodo anterior 
            if subnodo != Anterior:
                #Calculamos el numero de nodos en el subarbol del hijo
                Nodo_SubArbol = Recorrido(subnodo, nodo)
                # si el subarbol tiene un numero par de nodos, podemos cortar la arista
                if Nodo_SubArbol % 2 == 0:
                    ParCortes[0] += 1# incrementamos el contador de cortes
                else:
                    # si no es par, sumamos el tamano del subarbol al tamano del nodo actual
                    tamano += Nodo_SubArbol
        return tamano  # devolvemos el tamano total del subarbol 
    # Iniciamos el recorrido desde el nodo 1 
    Recorrido(1, -1) # -1 indica que no hay nodo anterior al inicio
    return ParCortes[0] # se devuelve el numero de cortes que se pueden hacer