import pandas as pd
df = pd.read_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivo_problemas_resueltos/archivo_datos.csv")
df["edad"] = df["edad"].astype (str)
print(type(df["edad"][0]))

#df["apellido"].replace("Bernuy","Bernoulli",inplace=True)
#print(df["apellido"])

print(df)
df = df.dropna()

df = df.drop_duplicates()

df.to_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivo_problemas_resueltos/archivo_datos_limpios.csv")