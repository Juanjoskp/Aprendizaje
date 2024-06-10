import re

text = "Este es un ejemplo para encontrar páginas web: https://www.marca.com"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern,text)

print(result)