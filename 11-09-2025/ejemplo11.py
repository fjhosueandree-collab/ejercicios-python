def func(*args, **kwargs):
    for a in args:
        print(a)
    for k, v in kwargs.items():
        print(k, ':', v)

# Ejemplo: Detalles de un proyecto
func(1, 2, 3, nombre='App Móvil', cliente='TechCorp', plazo='3 meses')
# Output:
# 1
# 2
# 3
# nombre : App Móvil
# cliente : TechCorp
# plazo : 3 meses
