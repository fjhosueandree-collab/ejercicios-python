try:
    anchura = int(input("Anchura de la línea: "))
    for i in range(anchura):
        print("+ ", end="")
except ValueError:
    print("Por favor, ingrese un número entero.")


    
try:
    anchura = int(input("Anchura de la línea: "))
    if anchura < 2:
        print("La anchura debe ser al menos 2.")
    else:
        print("* ", end="")
        for x in range(anchura - 2):
            print("= ", end="")
        print("* ")
except ValueError:
    print("Por favor, ingrese un número entero.")

    

try:
    altura = int(input("Altura de la figura: "))
    if altura < 2:
        print("La altura debe ser al menos 2.")
    else:
        print("* ")
        for x in range(altura - 2):
            print("|")
        print("* ")
except ValueError:
    print("Por favor, ingrese un número entero.")
