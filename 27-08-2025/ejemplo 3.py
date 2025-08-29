# Tupla con países
paises = ("Argentina", "Brasil",["China", 5.9],"Chile", "Brasil", "México")
print("Tupla de países:", paises)
# Usamos el método count() para contar cuántas veces aparece "Brasil"
print("Cantidad de veces que aparece 'Brasil':", paises.count("Brasil"))
# Usamos el método index() para encontrar el índice de "Chile"
print("Índice de 'Chile':", paises.index("Chile"))


paises[1].append("Corea") #tupla[1] hace referencia
print(paises)
