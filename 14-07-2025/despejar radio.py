# Importamos la librería "math" para poder usar funciones matemáticas como la raíz cuadrada (sqrt)
import math

# Paso 1: Tenemos el área del círculo (este dato ya lo conocemos)
area = 78.54

# Paso 2: Definimos el valor de pi (π), que se usa en fórmulas de círculos
pi = 3.14159

# Paso 3: Usamos la fórmula para despejar el radio:
# r = √(área / π)
radio = math.sqrt(area / pi)

# Paso 4: Calculamos el perímetro (también llamado circunferencia)
# Fórmula: perímetro = 2 × π × radio
perimetro = 2 * pi * radio

# Paso 5: Mostramos todos los resultados con solo 2 decimales
print(f" Área conocida: {area:.2f}")
print(f" Radio calculado usando raíz cuadrada: {radio:.2f}")
print(f" Perímetro del círculo: {perimetro:.2f}")
