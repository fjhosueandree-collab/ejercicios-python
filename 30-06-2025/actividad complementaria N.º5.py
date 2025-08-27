 numeros = []
...
... print("Ingresa 5 números: ")
...
... for i in range(5):
...     num = int(input(f"Número {i+1}: "))
...     numeros.append(num)
...
... contador_pares = 0
... for num in numeros:
...     if num % 2 == 0:
...         contador_pares += 1
...
... print(f"En la lista, hay {contador_pares} número(s) par(es). ")
