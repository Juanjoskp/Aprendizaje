def sumar_dos():
    while True:
        a = input("número 1: ")
        b = input("número 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            #print("Por favor, dame un número")
            print(f"ERRORf: {e}")    
        else:
            break
        finally:
            print("Jajajaj")
    return resultado
print(sumar_dos())