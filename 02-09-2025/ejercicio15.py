try:
    altura = int(input("Altura de la figura: "))
    if altura < 2:
        print("La altura debe ser al menos 2.")
    else:
        print("+ ")
        for i in range(altura - 2):
            print("|")
        print("+ ")
except ValueError:
    print("Por favor, ingrese un número entero.")
