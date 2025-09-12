frutas = {'Plátano': 0.8, 'Manzana': 1.2, 'Pera': 1.5, 'Naranja': 0.5}
try:
    fruta = input('¿Qué fruta quieres? ').title()
    kg = float(input('¿Cuántos kilos? '))
    if fruta in frutas:
        print(kg, 'kilos de', fruta, 'valen S/. ', frutas[fruta] * kg)
    else:
        print("Lo siento, la fruta", fruta, "no está disponible.")
except ValueError:
    print("Por favor, ingrese un número válido para los kilos.")
