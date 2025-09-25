def maxSubarray(arr):
    # ----------- Subarray (Kadane) -----------
    Acumulador = arr[0]   # Suma Maxima del subarreglo 
    ResultGlobal = arr[0]   # resultado global
    # recorremos desde el segundo elemento
    for i in range(1, len(arr)):
        # empezar un nuevo subarreglo o extender el actual
        Acumulador = max(arr[i], Acumulador + arr[i])
        # actualizo el resultado global si el acumulador es mayor
        ResultGlobal = max(ResultGlobal, Acumulador)
    # Si hay positivos, sumamos todos
    Sum_Max = sum(x for x in arr if x > 0)
    # Si no hay positivos, tomamos el máximo, osea el menos negativo
    if Sum_Max == 0:
        Sum_Max = max(arr)
    
    return [ResultGlobal, Sum_Max] # retornamos ambos resultados