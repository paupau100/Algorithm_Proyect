def tiene_longitud_minima (password,minima ):
    return len(password) >= minima

def tiene_letra_mayuscula (password):
    return any(c.isupper() for c in password)

def tiene_letra_minuscula (password):
    return any(c.islower() for c in password)

def tiene_digito (password):
    return any(c.isdigit() for c in password)   

def tiene_caracter_especial (password):
    caracteres_especiales = "!@#$%&*"
    return any(c in caracteres_especiales for c in password)

def evaluar_contraseña (password):
    contador =0
    if tiene_longitud_minima(password,8):
        contador +=1
    if tiene_letra_mayuscula(password):
        contador +=1
    if tiene_letra_minuscula(password):
        contador +=1
    if tiene_digito(password):
        contador +=1
    if tiene_caracter_especial(password):
        contador +=1
    if contador <=2:
        return "Contraseña débil"
    elif contador <=4:
        return "Contraseña media"
    else:
        return "Contraseña fuerte"
    
def probar_validador ():
    contraseñas = ["holaaa", "Python1", "Lala026*", "Segura2026!", "Clave@123"]
    for password in contraseñas:
        contraseña_limpia = password.strip()
        resultado = evaluar_contraseña(contraseña_limpia)
        print(f"Contraseña: {contraseña_limpia}")
        print(f"Evaluación: {resultado.upper()}")
        print("-" * 30)
def main():
    probar_validador()
if __name__ == "__main__":
    main()

 
