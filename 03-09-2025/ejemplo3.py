p = input('¿Qué marca de computadora tienes? ')
q = input('¿Cuánta capacidad de disco duro tiene (en GB o TB)? ')
r = input('¿Cuánta memoria RAM tiene (en GB)? ')
computadora = {'marca': p, 'disco_duro': q, 'ram': r}
print(computadora['marca'], 'tiene', computadora['disco_duro'], 'de disco duro y', computadora['ram'], 'de RAM')
