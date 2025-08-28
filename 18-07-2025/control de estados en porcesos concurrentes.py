permissions = 0b1010 # Permisos iniciales
new_permission = 0b0100 permissions |= new_permission # Añade permiso
print(bin(permissions)) # Salida: 0b1110
