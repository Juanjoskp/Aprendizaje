def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'
frase_resultante1 = frase("Juanjo", "Bernuy","es bobo")
print(frase_resultante1)

def frase(nombre,apellido,adjetivo = "es bobo"):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'
frase_resultante2 = frase("Juanjo", "Bernuy","es listo")
print(frase_resultante2)

def frase(nombre,apellido,adjetivo = "es bobo"):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'
frase_resultante3 = frase("Juanjo", "Bernuy")
print(frase_resultante3)