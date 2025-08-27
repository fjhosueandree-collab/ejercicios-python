
nombre = input("¿Cuál es tu nombre? ")

edad_str = input("¿Cuántos años tienes? ")

try:
    edad = int(edad_str)

 if: edad >= 18:    print(f"{nombre}, puedes votar.")
else:
    print(f"{nombre}, no puedes votar todavía.")
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")
