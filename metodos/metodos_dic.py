diccionario = {
    "nombre" : "Juanjo",
    "apellido" : "Bernuy",
    "voluntad" : 100
}

print(diccionario)

claves1 = diccionario.keys()

claves2 = diccionario.get("voluntGGad")
print("jajajaj")

print(claves2)

diccionario.pop("nombre")

print(diccionario)

diccionario_iterable = diccionario.items()

print(diccionario_iterable)