numero = int(input("Ingresa un número para verificar si es primo: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
