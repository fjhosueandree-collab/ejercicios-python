resultado = []
for i in [0, 1, 2]:  # Solo 0, 1, 2 para obtener los 12 valores deseados
    for j in [5, 6]:
        resultado.append(i * 2)  # Multiplicar i por 2
        resultado.append(j * 2)  # Multiplicar j por 2

print(*resultado)
