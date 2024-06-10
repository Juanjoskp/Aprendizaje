animales = ["perro", "gato", "loro", "leon","pez"]
numeros = [23,45,66,82,101]

for animal in animales:
    print(f'Ahora la variable es {animal}')

for numero in numeros:
    print(numero *10)

for numero,animal in zip(animales,numeros):
    print(f"recorriendo la lista 1 : {numero}")
    print(f"recorriendo la lista 2 : {animal}")

for num in range(10,20):
    print(num)
    
for num in range(10):
    print(num)

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(num)
    print(f'el indice es: {indice} y el valor es: {valor}')

for numero in numeros:
    print(f"ejecutando el último bucle, valor actual: {numero}")
else:
    print(f"el bucle termino")