import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

sns.histplot(data=df, x="Age", bins=30)
plt.savefig("hist.jpg")
plt.clf()

sns.countplot(
    data=df,
    x="Sex",
    hue="Survived"
)
plt.savefig("count.jpg")
plt.clf()


sns.barplot(
    data=df,
    x="Pclass",
    y="Age"
)
plt.savefig("bar.jpg")
plt.clf()

sns.boxplot(
    data=df,
    x="Pclass",
    y="Fare"
)
plt.savefig("box.jpg")
plt.clf()

sns.scatterplot(
    data=df,
    x="Age",
    y="Fare"
)
plt.savefig("scatter.jpg")
plt.clf()

correlacion = df.corr(numeric_only=True)
sns.heatmap(
    correlacion,
    annot=True,
    cmap="coolwarm"
)
plt.savefig("heat.jpg")