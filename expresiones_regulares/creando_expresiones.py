import re
texto = "el teléfono es +1 555 555 5555"
pattern = r'\+\d{1}\s\d{3}\s\d{3}\s\d{4}'
remplazo = re.sub(pattern,"(numero oculto)",texto)
print(remplazo)