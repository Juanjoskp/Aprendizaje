import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivo_problemas_graficos/cofla_ingresos.csv")
print(df)

sns.barplot(x="fuente",y="ingresos",data=df)

plt.show()

total_ingresos = df["ingresos"].sum()

print(f'El total de ingresos es de: ${total_ingresos} USD')