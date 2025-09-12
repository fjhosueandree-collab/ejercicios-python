def sum(*args):
    valor = 0
    for n in args:
        valor += n
    return valor

# Ejemplo 1: Original (10, 3) -> Agregamos 5
print(sum(10, 3, 5))  # Output: 18
# Ejemplo 2: Original (1, 2, 3) -> Agregamos 4
print(sum(1, 2, 3, 4))  # Output: 10
# Ejemplo 3: Original (3, 2, 4, 1) -> Agregamos 5
print(sum(3, 2, 4, 1, 5))  # Output: 15
# Ejemplo 4: Original () -> Agregamos 0
print(sum(0))  # Output: 0
print("Fin del programa")
