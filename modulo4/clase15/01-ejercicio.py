import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("titanic.csv")

# Ventajas de seaborn frente a matplotlib

# Matplotlib
# plt.hist(df["Age"])

# Seaborn:
# sns.histplot(data=dataframe, x="Age") <- Trabaja directamente con dataframes

# Histograma
# Analizar distribuciones
# en data le pasamos el dataframe, y en x, lo que va a ser el eje X
sns.histplot(data=dataframe, x="Age")
plt.title("Distribucion de edades")
plt.savefig("histograma.jpg")


plt.clf()

# Countplot
# Contar categorias
sns.countplot(data=dataframe, x="Pclass")
plt.title("Comparativa de clases")
plt.savefig("countplot.jpg")
plt.clf()

# Barplot
# Comparar promedios
sns.barplot(data=dataframe, x="Pclass", y="Fare")
plt.savefig("barplot.jpg")
plt.clf()


# Scatterplot
# Relaciones entre variables numericas
sns.scatterplot(data=dataframe, x="Age", y="Fare", hue="Survived")
plt.savefig("scatterplot.jpg")
plt.clf()

# Lineplot
# Muestra evolucion

sns.lineplot(data=dataframe, x="Pclass", y="Age")
plt.savefig("lineplot.jpg")
plt.clf()

# Boxplot
# Detecta Mediana, Dispersion y outliers

sns.boxplot(data=dataframe, y="Age")
plt.savefig("boxplot.jpg")
plt.clf()

# Violinplot
# Parecido al boxplot, pero detecta densidades.

sns.violinplot(data=dataframe, x="Sex", y="Age")
plt.savefig("violinplot.jpg")
plt.clf()
