a = int(input("Ingrese su CALIFICACION: "))

if a >= 18 and a <= 20:
    print("Está en la categoría Muy Bueno")
elif a >= 15 and a <= 17:
    print("Está en la categoría Bueno")
elif a >= 11 and a <= 14:
    print("Está en la categoría Regular")
elif a >= 8 and a <= 10:
    print("Está en la categoría Mal")
elif a >= 0 and a <= 7:
    print("Está en la categoría Deficiente")
else:
    print("Calificación ingresada no válida")
