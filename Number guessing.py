#Programa que elegira un numero random entre un rango de números y el usuario tratara de adivinar dicho el número.

import random

nombre = input('Hola, cual es tu nombre? ')
print(f'{nombre}, intenta adivinar el número que estoy pendando del 1 al 30.')
numero = random.randint(1, 30)
intentos = 0

while intentos < 5:
    eleccion = input('')
    eleccion = int(eleccion)
    intentos += 1

    if eleccion < numero:
        print('Lo siento, tu elección es muy baja.')
    
    if eleccion > numero:
        print('Lo siento, tu elección es muy alta.')

    if eleccion == numero:
        break

if eleccion == numero:
    print(f'Si!, es el número que estaba pensando. Lo hiciste en {intentos} intentos.')

if eleccion != numero:
    print(f'Perdiste!, el número que estaba pensando es {numero}')
