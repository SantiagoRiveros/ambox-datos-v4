import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_limpio.csv")

# Histograma de precios.
sns.histplot(
    data=df,
    x="price",
    kde=True
)
plt.savefig("./graficos/histograma-precios.jpg")
plt.clf()

# Countplot por estado del pedido.

sns.countplot(
    data=df,
    x="order_status"
)
plt.savefig("./graficos/countplot-estado-pedido.jpg")
plt.clf()
 
# Barplot del Top 10 categorías.

top = df.groupby(
"product_category_name_english"
)["Total_Venta"].sum().nlargest(10)

sns.barplot(
    x=top.values,
    y=top.index
)
plt.savefig("./graficos/barplot-top-10-categorias.jpg")
plt.clf()

# Boxplot del precio según categoría.

sns.boxplot(
    data=df,
    x="product_category_name_english",
    y="price"
)
plt.savefig("./graficos/boxplot-precio-categoria.jpg")
plt.clf()

# Countplot de compras por día de la semana.

sns.countplot(
    data=df,
    x="Dia"
)
plt.savefig("./graficos/countplot-compras-dia-semana.jpg")
plt.clf()

# Heatmap de correlación.

corr = df.select_dtypes("number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
plt.savefig("./graficos/heatmap.jpg")
plt.clf()