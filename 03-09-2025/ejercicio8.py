n = input('¿Cómo te llamas? ')
e = int(input('¿Cuántos años tienes? '))  # Convertir a entero
d = input('¿Cuál es tu dirección? ')
persona = {'n': n, 'e': e, 'd': d}
print(persona["n"], 'tiene', persona['e'], 'años y vive en', persona['d'])
