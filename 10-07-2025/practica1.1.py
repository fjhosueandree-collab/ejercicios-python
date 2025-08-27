print(" U+1F9EE Calculadora de operaciones básicas")
nombre = input("¿Cuál es tu nombre?")
print(f"Hola, (nombre). Vamos a realizar algunas operacioens.")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
división = num1 / num2
if num2 != 0 else "Indefinido (división por cero)"

print(f"\nResultados para (nombre):")
print(f"Suma: (num1) + (num2) = (suma)")
print(f"Resta: (num1) - (num2) = (resta)")
print(f"Multiplicación: (num1) * (num2) = (producto")
print(f"División: (num1) / (num2) = (división)")
