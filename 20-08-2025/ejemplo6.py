# -*- coding: utf-8 -*-
# Lista de ventas de la ferretería
ventas_ferreteria = []
# Registrar ventas de productos
ventas_ferreteria.append("martillo")
ventas_ferreteria.append("destornillador")
ventas_ferreteria.append("martillo")
ventas_ferreteria.append("clavos")
# Revisar cuántos martillos se vendieron
print("Martillos vendidos:", ventas_ferreteria.count("martillo"))
# Eliminar un producto de la lista
ventas_ferreteria.remove("clavos")
# Copiar la lista actual de ventas
ventas_backup = ventas_ferreteria.copy()
# Ordenar los productos alfabéticamente
ventas_ferreteria.sort()
print("Ventas ordenadas:", ventas_ferreteria)
# Insertar un nuevo producto en la posición 1
ventas_ferreteria.insert(1, "sierra")
print("Ventas tras insertar 'sierra':", ventas_ferreteria)
# Encontrar el índice de la primera aparición de "martillo"
print("Índice de 'martillo':", ventas_ferreteria.index("martillo"))
# Añadir más productos desde otra lista
nuevos_productos = ["taladro", "tornillos"]
ventas_ferreteria.extend(nuevos_productos)
print("Ventas tras añadir nuevos productos:", ventas_ferreteria)
# Extraer el último producto
producto_extraido = ventas_ferreteria.pop()
print("Producto extraído:", producto_extraido)
# Invertir el orden de las ventas
ventas_ferreteria.reverse()
print("Ventas invertidas:", ventas_ferreteria)
# Limpiar la lista de ventas al final del día
ventas_ferreteria.clear()
print("Ventas del día:", ventas_ferreteria)
print("Respaldo:", ventas_backup)
