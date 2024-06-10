frutas = ("platano", "ciruela", "manzana", "pera", "fresa", "melocotón")
cadena = "Juanjo Bernuy"
numero = [2,4,8,12]
for fruta in frutas:
    if fruta == "melocotón":
        continue
    print(f"Me voy a comer una {fruta}")
    if fruta == "fresa":
        break
else:
    print("Me he llenado")

for letra in cadena:
    print(letra)

numeros_al_cubo = [x**3 for x in numero]
print(numeros_al_cubo)