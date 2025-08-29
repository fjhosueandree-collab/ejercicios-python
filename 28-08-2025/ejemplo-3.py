lema = "CRECER JUNTOS"
letras_lema = [char for char in lema if char != " "]  # Letras del lema sin espacios
r = range(9, 1001, 9)  # De 9 en 9 hasta 1000

print(lema)  # Imprime: CRECER JUNTOS
print(letras_lema)  # Imprime: ['C', 'R', 'E', 'C', 'E', 'R', 'J', 'U', 'N', 'T', 'O', 'S']
print(f"Una lista: {list(r)} con longitud {len(r)}")  # Imprime: Una lista: [9, 18, ..., 999] con longitud 111
