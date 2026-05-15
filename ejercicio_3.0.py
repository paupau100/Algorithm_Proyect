def tiene_longitud_minima (password,minima ):#funcion para verificar la logitud minima 
    return len(password) >= minima
# Funciones para verificar cada criterio de seguridad
def tiene_letra_mayuscula (password):
    return any(c.isupper() for c in password)#verifica si hay alguna letra mayuscula en la contraseña usando any() y isupper()

def tiene_letra_minuscula (password):
    return any(c.islower() for c in password)#verifica si hay alguna letra minuscula en la contraseña usando any() y islower()

def tiene_digito (password):
    return any(c.isdigit() for c in password)   

def tiene_caracter_especial (password):
    caracteres_especiales = "!@#$%&*"
    return any(c in caracteres_especiales for c in password)
# elvalua la seguridad de la contraseña 
def evaluar_contraseña (password):# funcion para evaluar la contraseña 
    contador =0# contador para llevar la cuenta de los criterios cumplidos
    if tiene_longitud_minima(password,8):
        contador +=1# si cumple con la logitud suma 1 al contador
    if tiene_letra_mayuscula(password):
        contador +=1# si cumple con la letra mayuscula suma 1 al contador
    if tiene_letra_minuscula(password):
        contador +=1# si cumple con la letra minuscula suma 1 al contador
    if tiene_digito(password):
        contador +=1# si cumple con el digito suma 1 al contador
    if tiene_caracter_especial(password):
        contador +=1# si cumple con el caracter especial suma 1 al contador
    if contador <=2:# si el contador es menor o igual a 2 la contraseña es débil
        return "Contraseña débil"
    elif contador <=4:# si el contador es menor o igual a 4 la contraseña es media
        return "Contraseña media"
    else:# si el contador es mayor a 4 la contraseña es fuerte
        return "Contraseña fuerte"
    #validador de contraseñas para probar la función evaluar_contraseña con diferentes contraseñas de ejemplo
def probar_validador ():
    contraseñas = input("Ingrese las contraseñas separadas por comas: ").split(",")# solicita al usuario que ingrese las contraseñas separadas por comas y las divide en una lista 
# recorre la lista de contraseñas para evaluar cada una y mostrar el resultado
    for password in contraseñas:
        contraseña_limpia = password.strip()
        resultado = evaluar_contraseña(contraseña_limpia)
        print(f"Contraseña: {contraseña_limpia}")
        print(f"Evaluación: {resultado.upper()}")
        print("-" * 30)
 # la función main para ejecutar el programa
def main():
    probar_validador()
main()# llama a la función main para ejecutar el programa