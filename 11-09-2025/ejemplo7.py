def xx(**kwargs):
    for letra, numero in kwargs.items():
        print(letra, numero)

# Ejemplo: Características de un producto
print('Producto 1')
xx(precio=100, stock=50, descuento=10)
print('Producto 2')
xx(modelo='Laptop', año=2023)
# Output:
# Producto 1
# precio 100
# stock 50
# descuento 10
# Producto 2
# modelo Laptop
# año 2023
