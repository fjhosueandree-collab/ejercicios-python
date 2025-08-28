x = float(input("Ingrese 1er número: "))
y = float(input("Ingrese 2do número: "))

if y > 0:
    resultado = x * y
    print("La multiplicación es", resultado)
else:
    resultado = f'No se puede multiplicar {x} por {y}'
    print(resultado)
