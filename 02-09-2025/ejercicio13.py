try:
    anchura = int(input("Anchura de la línea: "))
    for i in range(anchura):
        print("+ ", end="")
except ValueError:
    print("Por favor, ingrese un número entero.")
