lista = list([1,2,3,4,5,67,101,"toma"])
cantidad_elementos = len(lista)

lista.append(99)

lista.insert(2,6174)

lista.extend([2030])

lista.pop(-2)

print(lista)

print(len(lista))

lista.pop(1)

lista.remove("toma")

#lista.clear()

lista.sort(reverse=True)

lista.sort()

#lista.reverse()

print(len(lista))

print(lista)

elemento_encontrado = lista.index(6174)

print(elemento_encontrado)