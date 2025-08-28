edad = int(input("Por favor, ingresa tu edad: "))

if edad < 18:
    print("No puedes comprar una propiedad porque eres menor de edad.")
elif edad >= 18:
    print("Puedes comprar una propiedad, tienes la mayoría de edad.")
else:
    print("Edad inválida, por favor ingresa un número válido.")

print("Recuerda que para menores de edad existen reglas especiales y consentimientos necesarios.")
