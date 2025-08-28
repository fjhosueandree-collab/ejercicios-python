nombre=input('Buenas noches, dime tu nombre: ')
print('Hola',nombre)
edad=int(input('¿Me dices tu edad? '))
if edad<18:
 print('todavia no votaras en elecciones')
 print(nombre,'todavía eres un menor')
 print('Espérate unos añitos')
elif edad==18:
 print('Estás en el límite')
else:
 print('Te estás haciendo mayor')
 print('Has dejado de ser menor')
