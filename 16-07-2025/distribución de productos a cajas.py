# Distribución de productos en cajas con más variables
total_productos = 47
capacidad_caja = 10
costo_caja = 3.50
costo_empaque = 1.20

cajas_completas = total_productos // capacidad_caja
productos_sobrantes = total_productos % capacidad_caja
costo_total_cajas = cajas_completas * costo_caja + costo_empaque

print(f"Cajas completas: {cajas_completas}")
print(f"Productos sobrantes: {productos_sobrantes}")
print(f"Costo total de las cajas: ${costo_total_cajas:.2f}")
