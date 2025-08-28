primer_termino = float(input("Ingresa el primer término (a1): "))
razon = float(input("Ingresa la razón de la progresión (r): "))
n = int(input("Ingresa el número de término que deseas calcular (n): "))

enesimo_termino = primer_termino * (razon ** (n - 1))

print(f"El término número {n} es: {enesimo_termino}")
