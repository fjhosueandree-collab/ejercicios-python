def doble_si_par(numero):
    if numero % 2 == 0:
        return numero * 2
    else:
        return "El número no es par."

valor_usuario = int(input("Ingresar un número: "))
resultado = doble_si_par(valor_usuario)
print("Resultado:", resultado)
