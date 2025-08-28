latencia = 45
carga = 70
if latencia < 50 and carga < 80:
 print("Enrutar tráfico al servidor")
elif latencia < 100 and carga < 90:
 print("Enrutar con precaución")
else:
 print("Desviar tráfico a otro servidor")
# Salida: Enrutar tráfico al servidor
