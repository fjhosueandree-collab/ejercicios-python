try:
    anchura = int(input("Anchura de la línea: "))
    if anchura < 2:
        print("La anchura debe ser al menos 2.")
    else:
        print("+ ", end="")
        for i in range(anchura - 2):
            print("- ", end="")
        print("+ ")
except ValueError:
    print("Por favor, ingrese un número entero.")
