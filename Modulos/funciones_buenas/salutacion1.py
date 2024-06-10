def saludar(name):
    return f'Hola {name}: espero que hayas tenido un buen día'

def saludar_raro(name):
    return f'Holiiii {name}: espero que hayas tenido un super meega buen día'

saludo = saludar("Juanjo")
print(saludo)
print(__name__)

saludo_raro = saludar_raro("Pepe")
print(saludo_raro)
print(__name__)

import modulo_saludar

saludo1 = modulo_saludar.saludar("Juanjo")
print(saludo1)