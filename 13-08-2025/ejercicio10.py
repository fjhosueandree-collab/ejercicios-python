i = 1
while i <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("Ok, lo has escrito en el intento", i)
        break
    i = i + 1
else:
    print("Has agotado tus tres intentos")
