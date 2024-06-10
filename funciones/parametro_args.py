#NO HE ENTENDIDO ESTO (4.40):
#def suma (nombre,*numeros):
#    return f'{nombre}, la suma de tus numeros es: {suma(numeros)}'

#resultado = suma("lucas",3,5,7,8,9,12,15,21)
#print(resultado)

#CORRECCIÓN DE CHAT GPT
def suma(nombre, *numeros):
    suma_total = sum(numeros)
    return f'{nombre}, la suma de tus números es {suma_total}'

resultado = suma("lucas", 3, 5, 7, 8, 9, 12, 15, 21)
print(resultado)

def suma_total (numeros):
    return sum([*numeros])

resultado2 = suma_total ([3, 5, 8, 7, 8, 9, 12, 15, 21])
print(resultado2)

