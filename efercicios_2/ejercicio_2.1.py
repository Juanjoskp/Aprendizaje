def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Introducir nombre del compañero: ")
        edad = int (input("Introducir la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor
asistente,profesor = obtener_compañeros(3)
print(f"El asistente es {asistente} y el profesor es {profesor}")