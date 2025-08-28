import pandas as pd
# DataFrame de ejemplo
data = {'producto_id': [101, 102, 103, 104], 'nombre': ['Teclado Mecánico', 'Mouse Gamer', 'Monitor 24"', 'Webcam HD'], 'stock': [35, 50, 25, 40]}
df_inventario = pd.DataFrame(data)
print("DataFrame Original:")
print(df_inventario)

# Extraemos los nombres de productos a una lista
lista_productos = df_inventario['nombre'].tolist()
print(f"\nLista de productos original: {lista_productos}")
# Añadimos un nuevo producto
nuevo_producto = "Auriculares Inalámbricos"
lista_productos.append(nuevo_producto)
print(f"Lista actualizada con append(): {lista_productos}")
