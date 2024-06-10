import modulo_saludar

saludo1 = modulo_saludar.saludar("Juanjo")
print(saludo1)
#print(type(modulo_saludar))

import modulo_saludar as m_saludar

saludo2 = m_saludar.saludar("Juanpi")
print(saludo2)
#print(type(m_saludar))

import modulo_saludar as m_saludar

from modulo_saludar import saludar
saludo3 = saludar("jj")
print(saludo3)

from modulo_saludar import saludar as saludar_normal, saludar_raro as saludo_julai
saludo4 = saludo_julai("Juanchi")
print(saludo4)
saludo5 = saludar_normal("Juanchi")
print(saludo5)

print(dir(m_saludar))

print(m_saludar.__name__)

print(__name__)