import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/jjbernuy/Downloads/JJ/vsc-cursito/Aprendizaje/archivo_problemas_graficos/pedos.csv")
print(df)

sns.lineplot(x="fecha",y="pedos",data=df)

plt.plot("01-09",17,"o")

plt.show()