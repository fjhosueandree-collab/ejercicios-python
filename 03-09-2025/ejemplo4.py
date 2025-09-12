try:
    peso = float(input('¿Cuál es tu peso en kg? '))
    altura = float(input('¿Cuál es tu altura en metros? '))
    indice_masa_corporal = {'peso': peso, 'altura': altura}
    print("\nDatos para el cálculo del IMC:")
    for clave, valor in indice_masa_corporal.items():
        print(clave.capitalize(), ":", valor)
    imc = indice_masa_corporal['peso'] / (indice_masa_corporal['altura'] ** 2)
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    if imc < 18.5:
        estado = "Falta de peso"
    elif 18.5 <= imc < 25:
        estado = "Normal"
    elif 25 <= imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    print(f"Estado según el IMC: {estado}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos para peso y altura.")

print(f"¡Felicitaciones! su estado de índice de masa corporal es {imc} usted se encuentra en un estado {estado}") 
