import random
# Tupla con 6 edades aleatorias entre 1 y 100
edades = tuple(random.randint(1, 100) for _ in range(6))
print("Tupla de edades aleatorias:", edades)
# Usamos el método count() para contar cuántas veces aparece una edad específica (ejemplo: 42)
print("Cantidad de veces que aparece la edad 42:", edades.count(42))
# Usamos el método index() para encontrar el índice de la primera edad mayor a 50
for edad in edades:
    if edad > 50:
        print("Índice de la primera edad mayor a 50:", edades.index(edad))
        break
else:
    print("No hay edades mayores a 50")
