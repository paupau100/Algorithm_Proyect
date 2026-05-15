# FUNCIONES DEL RETO 02: ESTADÍSTICAS DE NOTAS
# Calcula el promedio sumando las notas y dividiendo por la cantidad total [cite: 54, 55]
def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

# Retorna la nota más alta encontrada en la lista [cite: 57, 58]
def buscar_nota_mayor(notas):
    return max(notas) if notas else None

# Retorna la nota más baja encontrada en la lista [cite: 60, 61]
def buscar_nota_menor(notas):
    return min(notas) if notas else None

# Cuenta cuántos estudiantes superaron o igualaron la nota mínima [cite: 63, 64]
def contar_notas_aprobadas(notas, nota_minima):
    aprobados = 0
    for nota in notas:
        if nota >= nota_minima:
            aprobados += 1
    return aprobados

# Imprime la tabla con formato alineado de Nombre, Nota y Estado [cite: 66, 67, 68]
def mostrar_reporte(nombres, notas):
    # Uso de f-strings para alinear columnas según la pista [cite: 73]
    print(f"\n{'Nombre':<15} | {'Nota':<6} | {'Estado'}")
    print("-" * 35)
    for i in range(len(nombres)):
        # Determina si aprobó basado en el estándar de 3.0
        estado = "Aprobado" if notas[i] >= 3.0 else "Reprobado"
        print(f"{nombres[i]:<15} | {notas[i]:<6.1f} | {estado}")

# FUNCIONES DE ENTRADA Y PRUEBA

# Se encarga de pedir al usuario los nombres y las notas por teclado
def solicitar_datos():
    nombres = []
    notas = []
    # Se solicitan 5 estudiantes como requisito mínimo [cite: 69]
    print("Ingrese la información de 5 estudiantes:")
    
    for i in range(5):
        nombre = input(f"Nombre del estudiante {i+1}: ")
        nota = float(input(f"Nota de {nombre}: "))
        nombres.append(nombre)
        notas.append(nota)
    
    return nombres, notas

# Coordina la ejecución completa del reto 02 [cite: 23]
def probar_reto2():
    print("\n" + "="*10 + " CONFIGURACIÓN RETO 02 " + "="*10)
    
    # 1. Captura de datos dinámicos
    estudiantes, calificaciones = solicitar_datos()
    
    # 2. Muestra del reporte tabular [cite: 66]
    mostrar_reporte(estudiantes, calificaciones)
    
    # 3. Muestra de cálculos finales usando las funciones modulares
    print(f"\nResultados Estadísticos:")
    print(f"• Promedio del grupo: {calcular_promedio(calificaciones):.2f}")
    print(f"• Nota más alta: {buscar_nota_mayor(calificaciones)}")
    print(f"• Nota más baja: {buscar_nota_menor(calificaciones)}")
    print(f"• Total aprobados: {contar_notas_aprobadas(calificaciones, 3.0)}")
# ESTRUCTURA PRINCIPAL

# Punto de entrada que solo llama a la función de prueba [cite: 21]
def main():
    probar_reto2()

if __name__ == "__main__":
    main()