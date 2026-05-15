# 1. Intercambia valores entre dos posiciones de la lista [cite: 109]
def intercambiar(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 2. Algoritmo de ordenamiento que utiliza la función intercambiar [cite: 111, 112]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                intercambiar(arr, j, j + 1)

# 3. Busca un elemento de inicio a fin en la lista [cite: 114]
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

# 4. Busca un elemento dividiendo la lista (requiere lista ordenada) [cite: 116, 127]
def busqueda_binaria(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# 5. Muestra la lista con un formato visual claro [cite: 118]
def mostrar_array(arr, etiqueta):
    print(f"{etiqueta}: {arr}")

# Permite que el usuario cree su propia lista desordenada 
def solicitar_datos_busqueda():
    numeros = []
    print("Configuración de lista (5 números):")
    for i in range(5):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    return numeros

# --- COORDINACIÓN DEL RETO ---

# Ejecuta el flujo: pedir datos, mostrar, ordenar y buscar [cite: 121]
def probar_reto4():
    print("\n" + "="*10 + " CONFIGURACIÓN RETO 04 " + "="*10)
    
    # 1. El usuario crea la lista desordenada
    lista_usuario = solicitar_datos_busqueda()
    
    # 2. Mostrar lista inicial
    mostrar_array(lista_usuario, "\nLista ingresada")
    
    # 3. Ordenar la lista
    bubble_sort(lista_usuario)
    mostrar_array(lista_usuario, "Lista ordenada (Bubble Sort)")
    
    # 4. Buscar un elemento
    valor_buscado = int(input("\n¿Qué número desea buscar en la lista?: "))
    posicion = busqueda_binaria(lista_usuario, valor_buscado)
    
    # Mostrar resultado de la búsqueda
    if posicion != -1:
        print(f"¡Encontrado! El número {valor_buscado} está en el índice {posicion}.")
    else:
        print(f"El número {valor_buscado} no existe en la lista.")

# Punto de entrada obligatorio del programa [cite: 21, 23]
def main():
     probar_reto4()

if __name__ == "__main__":
    main()