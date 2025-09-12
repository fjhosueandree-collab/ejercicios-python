def read_list_args(*args):
    for count, arg in enumerate(args):
        print('%d - %s' % (count, arg))

# Ejemplo: Listar tareas pendientes
print("Tareas diarias")
read_list_args('Estudiar', 'Hacer ejercicio', 'Leer')
# Output:
# Tareas diarias
# 0 - Estudiar
# 1 - Hacer ejercicio
# 2 - Leer

print("Tareas semanales")
read_list_args('Comprar víveres', 2, 'Llamar a cliente', ['Lunes', 'Martes'])
# Output:
# Tareas semanales
# 0 - Comprar víveres
# 1 - 2
# 2 - Llamar a cliente
# 3 - ['Lunes', 'Martes']

print("Tareas varias")
read_list_args(1, "Reunión", 3.5, (10, 20), 'Finalizar informe')
# Output:
# Tareas varias
# 0 - 1
# 1 - Reunión
# 2 - 3.5
# 3 - (10, 20)
# 4 - Finalizar informe
