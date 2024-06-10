with open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/archivo.csv",encoding = "UTF-8") as archivo:
    print("Data leida correctamente")
    print(archivo.read())

    import csv
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
