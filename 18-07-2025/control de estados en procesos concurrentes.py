permissions = 0b1010101 # Permisos iniciales
new_permission = 0b0101100
permissions |= new_permission # Añade permiso
print(bin(permissions)) # Salida: 0b1111101
