diccionario = dict(nombre= "Juanjo", apellido= "Bernuy")

diccionario2 = {frozenset(["JJ","Juantx" ]):"Juanjo"}

print(diccionario2)

diccionario3 = dict.fromkeys(["nombre","apellido"])

print(diccionario3)

diccionario4 = dict.fromkeys("ABCDEFG","clase")

print(diccionario4)

diccionario5 = dict.fromkeys(["nombre", "apellido"],"clase")

print(diccionario5)