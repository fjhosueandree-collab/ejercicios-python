# Diccionario para mapear cada letra a la siguiente en el alfabeto
siguiente_letra = {
    'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 
    'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 
    'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V', 
    'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'
}

# Lista para almacenar las letras ingresadas
letras_ingresadas = []
letras_transformadas = []

# Pedir 6 letras al usuario
for _ in range(6):
    while True:
        letra = input("Ingrese una letra (A-Z): ").upper()
        if len(letra) == 1 and letra in siguiente_letra:
            letras_ingresadas.append(letra)
            nueva_letra = siguiente_letra.get(letra, letra)
            letras_transformadas.append(nueva_letra)
            print(f"Dame una {nueva_letra}")
            break
        else:
            print("Error: Por favor, ingrese una sola letra de A a Z.")

# Formar la palabra transformada
palabra = ''.join(letras_transformadas)
print(f"¡{palabra} VIVA!")
