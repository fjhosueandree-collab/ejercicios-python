# Repetir el bucle 10 veces
for repeticion in range(1, 11):
    print(f"\nRepetición {repeticion}:")
    i = 10
    print(f"El bucle no ha comenzado. Ahora i vale {i}")
    suma = 0
    for _ in range(10):  # Iterar 10 veces para pedir 10 números
        try:
            i = int(input("Ingrese un número entero: "))
            suma += i
            print(f"{i} * {i} * {i} = {i ** 3}")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            suma += 0  # No suma nada si la entrada es inválida
    print(f"El bucle ha terminado. Ahora i vale {i}")
    print(f"La suma de los valores ingresados es {suma}") 
