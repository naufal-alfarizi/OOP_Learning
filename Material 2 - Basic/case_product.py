import pandas as pd
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = float(price)

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"

data = pd.read_csv('dataset/Product.csv')

products = []

for index, row in data.iterrows():
    product = Product(row['name'], row['category'], row['price'])
    products.append(product)

print("List of Products:")
for product in products:
    print(product)

product_data = pd.DataFrame([{
    'Name': product.name,
    'Category': product.category,
    'Price': product.price
} for product in products])

print("\nProduct DataFrame:")
print(product_data)

plt.figure(figsize=(8, 6))
product_data.groupby('Category')['Price'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Price by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Price')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
