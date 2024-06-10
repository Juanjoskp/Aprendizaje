def saludar():
    print ("Hola, ¿Qué tal?")

saludar()

def saludar():
    print ("Hola, ¿Qué tal?")

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "crack"

    print(f"Hola {nombre}, que tal estás {adjetivo}?")

saludar("Juan","hombre")
saludar("Camila","MUJER")
saludar("Mario","trans")

def crear_contraseña_random(num):
    chars = "abcdefghi"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = (num - 2) % len(chars)
    c2 = num % len(chars)
    c3 = (num - 5) % len(chars)
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num
password = crear_contraseña_random(7)

frase = f"Tu contraseña nueva es {password}"
print(frase)

password,primer_numero = crear_contraseña_random(7)

print(f"Tu contraseña nueva es {password}")
print(f"el número utilizado ha sido el {primer_numero}")