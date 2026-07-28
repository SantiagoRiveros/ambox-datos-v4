import pandas as pd

df = pd.read_csv("ecommerce_limpio.csv")

# ¿Cuántos pedidos existen?

print("Cantidad de pedidos:", df["order_id"].nunique())

# ¿Cuánto dinero total se vendió?

print("Dinero total vendido:", df["Total_Venta"].sum())

# ¿Cuál es la categoría más vendida?

print("Categoria mas vendida:", df.groupby(
    "product_category_name_english"
)["Total_Venta"].sum().sort_values(
    ascending=False
).head(1))

# ¿Qué estado realiza más compras?

print("Estado con más compras:", df.groupby(
    "customer_state"
)["order_id"].count().sort_values(
    ascending=False
).head(1))

# ¿Qué ciudad compra más?

print("ciudad que compra más:", df.groupby(
    "customer_city"
)["order_id"].count().sort_values(
    ascending=False
).head(1))

# ¿Qué vendedor factura más?

print("vendedor que vennde más:", df.groupby(
    "seller_id"
)["Total_Venta"].sum().sort_values(
    ascending=False
).head(1))

# ¿Qué meses tienen mayores ventas?

print("meses con mayores ventas:", df.groupby(
    "Mes"
)["Total_Venta"].sum().head(3))

# ¿Cuál es el precio promedio?

print("precio promedio :", df["price"].mean())

# ¿Cuál es el costo promedio de envío?

print("costo promedio de envío:", df["freight_value"].mean())

# ¿Qué porcentaje de pedidos fueron entregados?

print("porcentaje entregado:", (
df["order_status"]
.eq("delivered")
.mean()
)*100)