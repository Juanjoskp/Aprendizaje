frase = input("Esta es la frase de muestra, hay que calcular cuanto se tarda en decirla")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f"Has dicho {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras / 2} en decirlas")
print(f"Dalto lo diría en {100 * cantidad_de_palabras // 2 *1.3 /100} segundos")
if cantidad_de_palabras > 120:
    print("No te enrolles")
