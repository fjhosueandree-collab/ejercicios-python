import os
...
... directorio_actual = os.getcwd()
... print(f"Directorio actual: {directorio_actual} ")
...
... contenido = os.listdir(directorio_actual)
... print("Contenido del directorio actual: ")
... for item in contenido:
...     print("-", item)
...
... nuevo_directorio = "mi_carpeta"
... if not os.path.exists(nuevo_directorio):
...     os.mkdir(nuevo_directorio)
...     print(f"Directorio '{nuevo_directorio}' creado. ")
... else:
...     print(f"El directorio '{nuevo_directorio}' ya existe. ")
