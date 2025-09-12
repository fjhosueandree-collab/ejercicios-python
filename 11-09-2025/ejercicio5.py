def read_list_args(*args):
    for count, arg in enumerate(args):
        print('%d - %s' % (count, arg))

print("Primero")
read_list_args('Ricardo', 'jarroba.com')
# Output:
# Primero
# 0 - Ricardo
# 1 - jarroba.com

print("Segundo")
read_list_args('Ricardo', 23, 'Ramon', [1, 2, 3], 'jarroba.com')
# Output:
# Segundo
# 0 - Ricardo
# 1 - 23
# 2 - Ramon
# 3 - [1, 2, 3]
# 4 - jarroba.com

print("Tercero")
read_list_args(10, "juan", 5.5, (5, 2, 0), 'cetpropuno.edu.pe', 0)
# Output:
# Tercero
# 0 - 10
# 1 - juan
# 2 - 5.5
# 3 - (5, 2, 0)
# 4 - cetpropuno.edu.pe
# 5 - 0
