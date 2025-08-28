sensores = [25, 999, 28, 1000, 22]
datos_validos = []
for valor in sensores:
    if 20 <= valor <= 30:
        datos_validos.append(valor)
print(f"Datos válidos: {datos_validos}")
# Salida: Datos válidos: [25, 28, 22]
