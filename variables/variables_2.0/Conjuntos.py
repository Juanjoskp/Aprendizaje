conjunto = set(["Dato 1"])

conjunto1 = frozenset(["dato1", "dato2", "dato3"])
conjunto2 = {conjunto1, "dato4"}

print(conjunto2)

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

resultado = conjunto1.issubset(conjunto2)
resultado2 = conjunto1 <= conjunto2

resultado3 = conjunto1.issuperset(conjunto2)
resultado4 = conjunto1 < conjunto2

resultado5 = conjunto1.isdisjoint(conjunto2)

print(resultado5)
