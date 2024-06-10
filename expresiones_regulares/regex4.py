import re
email = "example@example.com"
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-Z9.-]+\.[a-zA-Z]{2,}"
result = re.match(pattern,email)
if result:
    print("email válido")
else:
    print("email no válido")