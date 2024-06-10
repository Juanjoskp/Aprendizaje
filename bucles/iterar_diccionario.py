diccionario = {
    'Nombre' : "Juanjo",
    'Apellido 1' : "Bernuy",
    'Apellido 2' : "Badosa",
    'Apeelido 3' : "Mate",
    'Apellido 4' : "Quintana"
}
for key in diccionario:
    print(key)

for key in diccionario.items():
    print(key)

for key in diccionario:
    key
    print(f"La clave es: {key}")

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")