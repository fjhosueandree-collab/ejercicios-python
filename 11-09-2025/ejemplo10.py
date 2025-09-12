def cal_media(*args):
    if len(args) == 0:  # Evitar división por cero
        return 0
    total = 0
    for i in args:
        total += i
    resultado = total / len(args)
    return resultado

# Ejemplo: Promedio de gastos mensuales
a, b, c, d = 200, 300, 150, 250
media = cal_media(a, b, c, d)
print(media)  # Output: 225.0
print(cal_media(100, 200))  # Output: 150.0
print(cal_media(50, 100, 150))  # Output: 100.0
print(cal_media(500, 600, 700, 800))  # Output: 650.0
print("El gasto promedio es:")
print(media)  # Output: El gasto promedio es: 225.0
print("Programa terminado")
print(cal_media(10, 20, 30))  # Output: 20.0
