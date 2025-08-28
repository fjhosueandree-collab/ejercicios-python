import math

# Coeficientes de la ecuación cuadrática ax^2 + bx + c = 0
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

# Calculamos el discriminante: b^2 - 4ac
discriminante = b**2 - 4*a*c

# Aplicamos la fórmula general:
# x = (-b ± sqrt(discriminante)) / (2a)
if discriminante < 0:
    print("No hay soluciones reales porque el discriminante es negativo.")
elif discriminante == 0:
    x = (-b) / (2 * a)
    print(f"La ecuación tiene una única solución real: x = {x}")
else:
    raiz_discriminante = math.sqrt(discriminante)
    x1 = (-b + raiz_discriminante) / (2 * a)
    x2 = (-b - raiz_discriminante) / (2 * a)
    print(f"La ecuación tiene dos soluciones reales:")
    print(f"x1 = (-{b} + √{discriminante}) / (2 * {a}) = {x1}")
    print(f"x2 = (-{b} - √{discriminante}) / (2 * {a}) = {x2}")
