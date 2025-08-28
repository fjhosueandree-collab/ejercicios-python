edad_usuario = int(input("Por favor, ingresa tu edad: "))
if edad_usuario < 5:
    print("Tu DNI caduca cada 2 años.")
elif 5 <= edad_usuario < 30:
    print("Tu DNI tiene validez de 5 años.")
elif 30 <= edad_usuario < 70:
    print("Tu DNI tiene validez de 10 años.")
else:
    print("Tu DNI es permanente y no caduca.")
print("Gracias por usar el sistema de consulta.")
