curso = {'Matemáticas': 5, 'Física': 3, 'Química': 4}
t_valor = 0
for clave, valor in curso.items():
    print(clave, 'tiene', valor, 'créditos')
    t_valor += valor  # Forma más concisa
print('Número total de créditos del curso: ', t_valor)
