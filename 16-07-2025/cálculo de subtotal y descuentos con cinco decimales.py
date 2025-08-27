# 1. Cálculo de subtotal y descuento con más variables y 5 decimales
precio_producto1 = 59.95
precio_producto2 = 90.80
precio_producto3 = 35.40
subtotal = precio_producto1 + precio_producto2 + precio_producto3

descuento_producto1 = 10.00
descuento_producto2 = 8.00
descuento_producto3 = 7.50
descuento_total = descuento_producto1 + descuento_producto2 + descuento_producto3

impuestos = 12.30
total = subtotal - descuento_total + impuestos

print(f"Subtotal: ${subtotal:.5f}")
print(f"Descuento total: ${descuento_total:.5f}")
print(f"Impuestos: ${impuestos:.5f}")
print(f"Total después de descuento e impuestos: ${total:.5f}")
