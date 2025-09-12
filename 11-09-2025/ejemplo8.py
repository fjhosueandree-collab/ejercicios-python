def read_dict_args(**kwargs):
    for key, value in kwargs.items():
        print('%s - %s' % (key, value))

# Ejemplo: Detalles de eventos
print('Evento 1')
read_dict_args(tema='Conferencia', lugar='Auditorio', fecha='2025-10-01')
print('Evento 2')
read_dict_args(deporte='Fútbol', equipo='Real Madrid', estadio='Santiago Bernabéu')
print('Evento 3')
read_dict_args(curso='Programación', nivel='Intermedio', duracion=40)
print('Evento 4')
read_dict_args(nombre='Seminario', ponente='Ana López', ciudad='Madrid', aforo=100)
# Output:
# Evento 1
# tema - Conferencia
# lugar - Auditorio
# fecha - 2025-10-01
# Evento 2
# deporte - Fútbol
# equipo - Real Madrid
# estadio - Santiago Bernabéu
# Evento 3
# curso - Programación
# nivel - Intermedio
# duracion - 40
# Evento 4
# nombre - Seminario
# ponente - Ana López
# ciudad - Madrid
# aforo - 100
