capacidad_servidor = 30
latencia = 45
enrutar_trafico = capacidad_servidor > 20 or latencia < 50
print(enrutar_trafico) # Salida: True
