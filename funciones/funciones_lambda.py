multiplicar_por_tres = lambda x : x*3
print(multiplicar_por_tres(6))

numeros = (1,2,3,4,5,6,7,8,9,10,11,12)

def es_par(num):
    if (num%2==0):
        return True
    
def es_impar(num):
    if (num%2==1):
        return True    

numeros_pares = filter(es_par,numeros)
print(numeros_pares)
print(list(numeros_pares))

numeros_impares = filter(es_impar,numeros)
print(numeros_impares)
print(list(numeros_impares))

numeros_pares_lambda = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares_lambda))
