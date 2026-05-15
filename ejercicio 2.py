def calcular_promedio(notas):
    # Calcula la suma de las notas y divide por el total de elementos
    if not notas:
        return 0
    return sum(notas) / len(notas)

def buscar_nota_mayor(notas):
    # Retorna el valor máximo encontrado en la lista
    if not notas:
        return None
    return max(notas)

def buscar_nota_menor(notas):
    # Retorna el valor mínimo encontrado en la lista
    if not notas:
        return None
    return min(notas)

def contar_notas_aprobadas(notas, nota_minima):
    # Cuenta cuántos estudiantes superaron o igualaron la nota mínima
    aprobados = 0
    for nota in notas:
        if nota >= nota_minima:
            aprobados += 1
    return aprobados

def mostrar_reporte(nombres, notas):
    # Imprime la tabla con formato alineado
    print(f"\n{'Nombre':<15} | {'Nota':<6} | {'Estado'}")
    print("-" * 35)
    for i in range(len(nombres)):
        # Lógica de estado: aprobado si es >= 3.0
        estado = "Aprobado" if notas[i] >= 3.0 else "Reprobado"
        print(f"{nombres[i]:<15} | {notas[i]:<6.1f} | {estado}")

def probar_reto2():
    # Función para organizar y ejecutar las pruebas del reto
    print("\n" + "="*10 + " RESULTADOS DEL RETO 02 " + "="*10)
    
    # Datos de ejemplo (mínimo 5 estudiantes)
    estudiantes = ["Juan", "María", "Carlos", "Ana", "Luis"]
    calificaciones = [4.5, 2.8, 3.5, 5.0, 1.5]
    
    # Ejecución de funciones
    mostrar_reporte(estudiantes, calificaciones)
    
    print(f"\nResumen Estadístico:")
    print(f"• Promedio: {calcular_promedio(calificaciones):.2f}")
    print(f"• Nota Máxima: {buscar_nota_mayor(calificaciones)}")
    print(f"• Nota Mínima: {buscar_nota_menor(calificaciones)}")
    print(f"• Total Aprobados: {contar_notas_aprobadas(calificaciones, 3.0)}")

# --- ESTRUCTURA PRINCIPAL ---

def main():
    # La función principal solo llama a los retos
    probar_reto2()

if __name__ == "__main__":
    # Punto de inicio del programa
    main()
def calcular_promedio(notas):
    # Calcula la suma de las notas y divide por el total de elementos
    if not notas:
        return 0
    return sum(notas) / len(notas)

def buscar_nota_mayor(notas):
    # Retorna el valor máximo encontrado en la lista
    if not notas:
        return None
    return max(notas)

def buscar_nota_menor(notas):
    # Retorna el valor mínimo encontrado en la lista
    if not notas:
        return None
    return min(notas)

def contar_notas_aprobadas(notas, nota_minima):
    # Cuenta cuántos estudiantes superaron o igualaron la nota mínima
    aprobados = 0
    for nota in notas:
        if nota >= nota_minima:
            aprobados += 1
    return aprobados

def mostrar_reporte(nombres, notas):
    # Imprime la tabla con formato alineado
    print(f"\n{'Nombre':<15} | {'Nota':<6} | {'Estado'}")
    print("-" * 35)
    for i in range(len(nombres)):
        # Lógica de estado: aprobado si es >= 3.0
        estado = "Aprobado" if notas[i] >= 3.0 else "Reprobado"
        print(f"{nombres[i]:<15} | {notas[i]:<6.1f} | {estado}")

def probar_reto2():
    # Función para organizar y ejecutar las pruebas del reto
    print("\n" + "="*10 + " RESULTADOS DEL RETO 02 " + "="*10)
    
    # Datos de ejemplo (mínimo 5 estudiantes)
    estudiantes = ["Juan", "María", "Carlos", "Ana", "Luis"]
    calificaciones = [4.5, 2.8, 3.5, 5.0, 1.5]
    
    # Ejecución de funciones
    mostrar_reporte(estudiantes, calificaciones)
    
    print(f"\nResumen Estadístico:")
    print(f"• Promedio: {calcular_promedio(calificaciones):.2f}")
    print(f"• Nota Máxima: {buscar_nota_mayor(calificaciones)}")
    print(f"• Nota Mínima: {buscar_nota_menor(calificaciones)}")
    print(f"• Total Aprobados: {contar_notas_aprobadas(calificaciones, 3.0)}")

# --- ESTRUCTURA PRINCIPAL ---

def main():
    # La función principal solo llama a los retos
    probar_reto2()

if __name__ == "__main__":
    # Punto de inicio del programa
    main()
