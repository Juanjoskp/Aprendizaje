nombres = ["Juanjo","Gorka","Ane","Alex","Sofia"]
apellidos = ["Bernuy","Martin","Aguilar","Juaristi","Ceballos"]

with open("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivo_problemas_resueltos/nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]

    for n,a in zip(nombres,apellidos):
        arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n")