#archivo1 = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
#print(archivo1.read())

#archivo_sin_leer = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
#archivo2 = archivo_sin_leer.read()
#linea_1 = archivo_sin_leer.readline()
#print(linea_1)

#archivo_sin_leer = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
#archivo3 = archivo_sin_leer.read()
#lineas = archivo_sin_leer.readlines()
#print(lineas)

#archivo_sin_leer = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
#lineas = archivo_sin_leer.readlines()
#print(lineas)

archivo_sin_leer = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
linea = archivo_sin_leer.readline()
print(linea)

archivo_sin_leer.close()

archivo_sin_leer = open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt")
linea = archivo_sin_leer.readline(10)
print(linea)

archivo_sin_leer.close()