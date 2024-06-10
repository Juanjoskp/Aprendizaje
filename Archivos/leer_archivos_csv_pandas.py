import pandas as pd
df = pd.read_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/archivo.csv")
df2 = pd.read_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivos/archivo.csv")
#print(df)
#print(df["Nombre"])
#,names=["Name","Last name","Age"]

nombres = df["Nombre"]

#cadena = "0123456789"

#print(cadena[1:6])

#print(df)

df_ordenado_ascendente = df.sort_values("edad")

df_ordenado_descendente = df.sort_values("edad",ascending=False)



#print(df_ordenado_ascendente)
#print(df_ordenado_descendente)

df_concatenado = pd.concat([df,df2])
print(df_concatenado)

primeras_filas = df.head(2)
print(primeras_filas)

ultimas_filas = df.tail(2)
print(ultimas_filas)

filas_totales,columnas_totales = df.shape
print(filas_totales,columnas_totales)

df_info = df.describe()
print(df_info)

elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)

elemento_especifico_iloc = df.iloc[2,1]
print(elemento_especifico_iloc)

apellidos = df.iloc[:,1]
print(apellidos)

fila_3 = df.loc[2,:]
fila_4 = df.iloc[2,:]
print(fila_4)

accediendo_a_fila_mayor_que_40 = df.loc[df["edad"]>40,:]
print(accediendo_a_fila_mayor_que_40)


