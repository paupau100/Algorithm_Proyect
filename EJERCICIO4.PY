# 1. Crea: intercambiar(arr, i, j) [cite: 109]
def intercambiar(arr, i, j):
    # Intercambia los valores en las posiciones i y j de la lista
    arr[i], arr[j] = arr[j], arr[i]

# 2. Crea: bubble_sort(arr) - Debe llamar a intercambiar() [cite: 111, 112]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Llamada obligatoria a la función de intercambio 
                intercambiar(arr, j, j + 1)

# 3. Crea: busqueda_lineal(arr, objetivo) [cite: 114]
def busqueda_lineal(arr, objetivo):
    # Recorre la lista de inicio a fin buscando el objetivo
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

# 4. Crea: busqueda_binaria(arr, objetivo) [cite: 116]
def busqueda_binaria(arr, objetivo):
    # La búsqueda binaria usa inicio, fin y medio 
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

# 5. Crea: mostrar_array(arr, etiqueta) [cite: 118]
def mostrar_array(arr, etiqueta):
    # Imprime la etiqueta y la lista con formato [cite: 120]
    print(f"{etiqueta}: {arr}")

# 6. Función de Prueba [cite: 121]
def probar_reto4():
    print("\n" + "="*10 + " RETO 04: ORDENADOR Y BUSCADOR " + "="*10)
    
    # Crear lista desordenada [cite: 122]
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    # Mostrarla [cite: 123]
    mostrar_array(numeros, "Lista Inicial (Desordenada)")
    
    # Ordenarla [cite: 124]
    bubble_sort(numeros)
    mostrar_array(numeros, "Lista Final (Ordenada)")
    
    # Buscar elementos [cite: 125]
    objetivo = 22
    # Se utiliza búsqueda binaria porque la lista ya está ordenada
    posicion = busqueda_binaria(numeros, objetivo)
    
    if posicion != -1:
        print(f"\nResultado: El número {objetivo} está en el índice {posicion}.")
    else:
        print(f"\nResultado: El número {objetivo} no se encuentra en la lista.")

def main():
    # La función main() sólo debe llamar funciones [cite: 21, 23]
    probar_reto4()

if __name__ == "__main__":
    main()
