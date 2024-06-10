with open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/texto_de_dalto.txt","a",encoding = "UTF-8") as archivo:
    #print("hola")
    #archivo.write("\n")
    #archivo.write(f"dd\n")
    #archivo.write(f"aa\n")
    #archivo.write(f"cc\n")

        archivo.write("\n")
        for i in range(2):
            archivo.write(f'linea {i+i} agregada\n')