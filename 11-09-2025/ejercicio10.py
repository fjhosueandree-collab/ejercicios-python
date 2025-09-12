def cal_media(*args):
    if len(args) == 0:  # Evitar división por cero
        return 0
    total = 0
    for i in args:
        total += i
    resultado = total / len(args)
    return resultado

a, b, c, d, e = 3, 5, 10, 15, 160
media = cal_media(a, b, c, d, e)
print(media)  # Output: 38.6
print(cal_media(12, 11))  # Output: 11.5
print(cal_media(2, 20, 15))  # Output: 12.333333333333334
print(cal_media(100, 500, 600, 700))  # Output: 475.0
print("La media es:")
print(media)  # Output: La media es: 38.6
print("Programa terminado")
print(cal_media(2, 3, 4))  # Output: 3.0
