def xx(**kwargs):
    for letra, numero in kwargs.items():
        print(letra, numero)

print('Primero')
xx(uno=1, dos=2, tres=3, cuatro=4)
print('Segundo')
xx(juan=30, pedro=40)
# Output:
# Primero
# uno 1
# dos 2
# tres 3
# cuatro 4
# Segundo
# juan 30
# pedro 40
