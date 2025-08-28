edad = int(input("Por favor, ingresa tu edad: "))

if edad < 18:
    print("No puedes votar porque no eres mayor de edad.")
elif 18 <= edad <= 70:
    print("Eres mayor de edad y el voto es obligatorio.")
else:
    print("Tienes más de 70 años y el voto ya no es obligatorio; es voluntario.")

print("Recuerda que ejercer el voto es un derecho fundamental.")
