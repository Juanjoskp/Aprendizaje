import re

texto = '''Besos que Vienen riendo 1. abb, 
luego llorando se van 222 aaabbbbabbaba, 
y en ellos se va la vida, que nunca más volverán 3
capitan'''

resultado= re.findall(r"\d",texto)
print(resultado)

resultado1= re.search("besos",texto,flags=re.IGNORECASE)
print(resultado1)

resultado2= re.findall("vi",texto,flags=re.IGNORECASE)
print(resultado2)

resultado3= re.findall(r"\D",texto)
print(resultado3)

resultado4= re.findall(r"\w",texto)
print(resultado4)

resultado5= re.findall(r"\W",texto)
print(resultado5)

resultado6= re.findall(r"\s",texto)
print(resultado6)

resultado7= re.findall(r"\S",texto)
print(resultado7)

resultado8= re.findall(r"\.",texto)
print(resultado8)

resultado9= re.findall(r"\n",texto)
print(resultado9)

resultado10= re.findall(r".",texto)
print(resultado10)

resultado11= re.findall(r"\,",texto)
print(resultado11)

resultado12= re.findall(r"\d\.\s",texto)
print(resultado12)

resultado13= re.findall(r"^Besos",texto)
print(resultado13)

resultado14= re.findall(r"^luego",texto,flags=re.M)
print(resultado14)

resultado15= re.findall(r"capitan$",texto,flags=re.M)
print(resultado15)

resultado16= re.findall(r"\d{3}\s",texto)
print(resultado16)

resultado17= re.findall(r"\d{1,2}",texto)
print(resultado17)

resultado18= re.findall(r"(ab){1,2}",texto)
print(resultado18)

resultado19= re.findall(r"[ab]{1,2}",texto)
print(resultado19)

resultado20= re.findall(r"[ab]{1,2}|Besos",texto)
print(resultado20)