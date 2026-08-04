import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("dataset.csv")

# Histograma - Distribucion de edades

sns.histplot(data=df, x="Age", kde=True)
plt.title("Histograma - Distribucion de edades")
plt.savefig("./graficos/Histograma - Distribucion de edades.jpg")
plt.clf()

# Countplot - Asistencia

sns.countplot(data=df, x="No-show")
plt.title("Countplot - Asistencia")
plt.savefig("./graficos/Countplot - Asistencia.jpg")
plt.clf()

# Countplot - Sexo
sns.countplot(data=df, x="Gender")
plt.title("Countplot - Sexo")
plt.savefig("./graficos/Countplot - Sexo.jpg")
plt.clf()

# Barplot - Edad promedio por asistencia
sns.barplot(data=df, x="No-show", y="Age")
plt.title("Barplot - Edad promedio por asistencia")
plt.savefig("./graficos/Barplot - Edad promedio por asistencia")
plt.clf()

# Boxplot - Edad y asistencia
sns.boxplot(data=df,x="No-show", y="Age")
plt.title("Boxplot - Edad y asistencia")
plt.savefig("./graficos/Boxplot - Edad y asistencia")
plt.clf()

# Convertimos la columna No-show
df["No-show"] = df["No-show"].map({
    "No": 0,
    "Yes": 1
})

# Countplot - Asistencia y Genero
sns.countplot(data=df,x="Gender", hue="No-show")
plt.xlabel("Genero")
plt.ylabel("Cantidad de pacientes")
plt.legend(["Asistio", "No asistio"])
plt.title("Countplot - Asistencia y Genero")
plt.savefig("./graficos/Countplot - Asistencia y Genero")
plt.clf()


# Heatmap

corr = df.select_dtypes("number").corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.savefig("./graficos/Heatmap")