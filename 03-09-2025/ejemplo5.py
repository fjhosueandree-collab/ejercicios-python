try:
    accesorios_electronicos = {
        'Teclado': 150.0,
        'Ratón': 60.0,
        'Monitor': 1000.0,
        'Auriculares': 200.0,
        'Telefono': 500.0 
    }
    accesorio = input('¿Qué accesorio electrónico quieres? ').title()
    unidades = float(input('¿Cuántas unidades? '))
    if accesorio in accesorios_electronicos:
        print(unidades, 'unidades de', accesorio, 'valen S/.', accesorios_electronicos[accesorio] * unidades)
    else:
        print("Lo siento, el accesorio", accesorio, "no está disponible.")
except ValueError:
    print("Por favor, ingrese un número válido para las unidades.")
