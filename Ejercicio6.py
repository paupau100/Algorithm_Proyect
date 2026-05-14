#Calculadora modular
#Primero la potenciación,usando una función que llamaremos 'potenciación(base,exp)'
def potencia(base, exp):
    if exp == 0: #decimos que si exp es igual a cero nos devuelva 1 porque x**0=1
        return 1
    return base * potencia(base, exp - 1) #Llamamos a la función potencia para que se multiplique por la base pero que se le reste 1 al exponente

#Ahora vamos con el máximo común denominador 
def mcd(a, b): #Definimos la función que alberga ambos números
    if b == 0:
        return a
    return mcd(b, a % b)



def es_primo(n, div=2):
    if n < 2:
        return False
    if n == div:
        return True
    if n % div == 0:
        return False
    return es_primo(n, div + 1)


def fibonacci(k):
    if k == 0: return 0
    if k == 1: return 1
    return fibonacci(k - 1) + fibonacci(k - 2)


def generar_serie_fibonacci(m, actual=0, serie=None):
    if serie is None: serie = []
    if actual == m: return serie
    serie.append(fibonacci(actual))
    return generar_serie_fibonacci(m, actual + 1, serie)



historial = []


def agregar_al_historial(nombre_op, resultado):
    
    registro = f"{nombre_op.upper()} -> Resultado: {resultado}"
    historial.append(registro)


def mostrar_historial():
    
    print("\n --- HISTORIAL DE OPERACIONES --- ")
    if not historial:
        print("Vacío.")
    else:
        for elemento in historial:
            print(f"• {elemento}")


def ejecucion_potencia():
    d=int(input('Base: '))
    e=int(input('Exponente: '))
    valor_calculado=potencia(d,e)
    print(f'resultado:{valor_calculado}')
    agregar_al_historial('potencia',valor_calculado)


def ejecutar_mcd():
    a = int(input("Número A: "))
    b = int(input("Número B: "))
    valor_calculado = mcd(a, b)
    print(f"MCD: {valor_calculado}")
    agregar_al_historial("mcd", valor_calculado)


def ejecutar_primo():
    n = int(input("Número: "))
    es_p = es_primo(n)
    # Usamos .upper() para recalcar la respuesta
    texto_valor = "ES PRIMO".upper() if es_p else "NO ES PRIMO".upper()
    print(texto_valor)
    agregar_al_historial("verificar primo", texto_valor)


def ejecutar_fibonacci():
    entrada = input("¿Cuántos números quieres?: ")
    # Uso de .isdigit() para validar
    if entrada.isdigit():
        m = int(entrada)
        valor_calculado = generar_serie_fibonacci(m)
        print(valor_calculado)
        agregar_al_historial("fibonacci", valor_calculado)
    else:
        print("Error: Solo se permiten números.")


def main():
    while True:
        print('\n---Menú---\n| 1. Potencia \n| 2. MCD \n| 3. Número Primo \n| 4. Lista Fibonacci \n| 5. Historial \n| 6. Salir')
        opcion=input('Seleccionar: ').strip()

        match opcion:
            case '1': ejecucion_potencia()
            case '2': ejecutar_mcd()
            case '3': ejecutar_primo()
            case '4': ejecutar_fibonacci()
            case '5': mostrar_historial()
            case '6': break 
            case _: print('Opción inválida.')
if __name__ == "__main__":
    main()