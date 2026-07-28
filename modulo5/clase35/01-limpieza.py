import pandas as pd

orders = pd.read_csv("./csv/olist_orders_dataset.csv")

order_items = pd.read_csv("./csv/olist_order_items_dataset.csv")

products = pd.read_csv("./csv/olist_products_dataset.csv")

customers = pd.read_csv("./csv/olist_customers_dataset.csv")

translation = pd.read_csv("./csv/product_category_name_translation.csv")


products = products.merge(
    translation,
    on="product_category_name",
    how="left"
)
# ahora productos tiene una columna nueva

df = orders.merge(
    order_items,
    on="order_id",
    how="inner"
)



df = df.merge(
    products,
    on="product_id",
    how="left"
)

df = df.merge(
    customers,
    on="customer_id",
    how="left"
)


print(df.columns)



df = df.dropna(subset=["order_approved_at"])

df["product_category_name"] = df[
    "product_category_name"
].fillna("Unknown")

df["product_category_name_english"] = df[
    "product_category_name_english"
].fillna("Unknown")

df = df.drop(columns=["product_name_lenght"])

df = df.drop(columns=["product_photos_qty"])



df["product_weight_g"] = df[
    "product_weight_g"
].fillna(
    df["product_weight_g"].median()
)

df["product_length_cm"] = df[
    "product_length_cm"
].fillna(
    df["product_length_cm"].median()
)

df["product_height_cm"] = df[
    "product_height_cm"
].fillna(
    df["product_height_cm"].median()
)

df["product_width_cm"] = df[
    "product_width_cm"
].fillna(
    df["product_width_cm"].median()
)

df = df.drop(columns=["product_description_lenght"])


print(df.isnull().sum())


print(df.duplicated())

df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"]
)

df["Total_Venta"] = df["price"] + df["freight_value"]

df["Mes"] = df["order_purchase_timestamp"].dt.month_name()

df["Año"] = df["order_purchase_timestamp"].dt.year

df["Dia"] = df["order_purchase_timestamp"].dt.day_name()

df["Fin_Semana"] = df["order_purchase_timestamp"].dt.weekday >= 5

df.to_csv(
    "ecommerce_limpio.csv",
    index=False
)
