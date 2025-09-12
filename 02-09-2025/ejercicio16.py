try:
    alto = int(input("Introduce la altura: "))
    largo = int(input("ahora la longitud: "))
    if alto < 1 or largo < 1:
        print("La altura y la longitud deben ser al menos 1.")
    else:
        for a in range(alto):
            for l in range(1, largo):
                print("*", end=" ")
            print("-")
except ValueError:
    print("Por favor, ingrese números enteros.")
