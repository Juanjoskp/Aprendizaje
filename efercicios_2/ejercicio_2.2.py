def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado1 = primos_hasta(98)
print(resultado1)

#mejora con ChatGP en caso de 2 (aunque no es necesario, pero no é porqué)
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

resultado = es_primo(98)
print(resultado)

