""" Я, к сожалению еще не знаком с библиотекой pySpark, (почитав в "гугле" о чем это, понял, что можно предложить вариант на Pandas)"""
import pandas as pd

# Примерные данные для продуктов
products_data = {
    "product_id": [1, 2, 3],
    "product_name": ["Product A", "Product B", "Product C"]
}
products_df = pd.DataFrame(products_data)

# Примерные данные для категорий
categories_data = {
    "category_id": [1, 2],
    "category_name": ["Category X", "Category Y"]
}
categories_df = pd.DataFrame(categories_data)

# Примерные данные для связей продуктов и категорий
product_category_data = {
    "product_id": [1, 1, 2],
    "category_id": [1, 2, 1]
}
product_category_df = pd.DataFrame(product_category_data)

# Объединение датафреймов для получения пар "Имя продукта - Имя категории"
product_category_pairs_df = product_category_df \
    .merge(products_df, on="product_id") \
    .merge(categories_df, on="category_id") \
    .loc[:, ["product_name", "category_name"]]

# Получение продуктов, у которых нет категорий
products_with_categories_df = product_category_df[["product_id"]].drop_duplicates()
products_without_categories_df = products_df[~products_df["product_id"].isin(products_with_categories_df["product_id"])] \
    .loc[:, ["product_name"]]

# Показ результатов
print("Пары 'Имя продукта - Имя категории':")
print(product_category_pairs_df)

print("\nПродукты без категорий:")
print(products_without_categories_df)
