import math

a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La ecuación tiene una solución real: x = {x}")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones reales son: x1 = {x1} y x2 = {x2}")
