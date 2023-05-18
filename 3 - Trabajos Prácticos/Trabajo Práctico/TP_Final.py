"""Trabajo práctico de AED N°1 """

__author__ = "Grupo 147 _ AED Sistemas _ FRC _ UTN _ Argentina "

import random

# Presentación, reglas e ingreso de nombres

print('**********\n¡Bienvenidos al juego de dos o tres!\n********\n')
print('**********\nReglas del juego\n')
print('Se juega de a dos jugadores, por turnos. Cada uno participará en dos rondas con diferentes reglas cada una.')
print('En la primera, deberán lanzar tres dados; si los tres salen iguales, sumarán 6 puntos.')
print('Si dos son iguales, podrá relanzar el distinto con la posibilidad de que salga igual a los anteriores y sumar 6 '
      'puntos, o que vuelva a salir distinto y sumar tan solo 3')
print('Si salen los 3 distintos, no sumará ningún punto')
print(
    'En la ronda dos, volverán a lanzar tres dados pero antes, deberán adivinar si la suma de los tres será par o impar')
print(
    'Si el jugador adivinó correctamente a que paridad corresponde la suma de los dados, sumará el valor del dado mayor '
    'a su puntaje. Caso contrario, restará el valor del dado menor.'
    'Si los tres dados son de la paridad elegida, se duplicará su puntaje. ')
print('**********\n')
input('Si entendió, presione enter para comenzar a jugar...')
nombre_1 = input('Ingrese el nombre del jugador N°1: ')
nombre_2 = input('Ingrese el nombre del jugador N°2: ')
print('\n**********', nombre_1, 'preparese para jugar')

# Comienza el juego, ronda 1, jugador numero 1

input('Presione enter para tirar los dados')
dado1 = random.randrange(1, 7)
dado2 = random.randrange(1, 7)
dado3 = random.randrange(1, 7)
print('Sus dados son: "', dado1, '", "', dado2, '" y "', dado3, '"')
input('Presione enter para continuar')

if dado1 == dado2 and dado1 == dado3:
    puntos1 = 6
    print('Los 3 dados de ', nombre_1, ' son iguales, suma 6 puntos')

# Si los dos primeros dados son iguales (el tercero es distinto)

elif dado1 == dado2:
    print(dado1, ' y ', dado2, 'son iguales, puede relanzar el tercer dado que antes había sido de ', dado3,
          ' y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado3 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado3)
    if dado1 == dado3:
        puntos1 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado3, 'así que gana tan solo 3 puntos')
        puntos1 = 3

# Si el ultimo y primer dado son iguales (el segundo es distinto)

elif dado1 == dado3:
    print(dado1, ' y ', dado3, 'Son iguales, deberá relanzar el segundo dado que antes había sido de ', dado2,
          'y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado2 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado2)
    if dado1 == dado2:
        puntos1 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado2, 'así que gana tan solo 3 puntos')
        puntos1 = 3

# Si el segundo y tercer dado son iguales (el primero es distinto)

elif dado2 == dado3:
    print(dado2, ' y ', dado3, 'Son iguales, deberá relanzar el primer dado que antes había sido de ', dado1,
          'y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado1 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado1)
    if dado1 == dado2:
        puntos1 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado1, 'así que gana tan solo 3 puntos')
        puntos1 = 3

# Si ningún dado es igual, todos distintos

else:
    print('Todos los dados son distintos, así que no sumó ningún punto')
    puntos1 = 0

# Ronda 1, Jugador numero 2

print('\n**********', nombre_2, 'preparese para jugar')
input('Presione enter para tirar los dados')

dado1 = random.randrange(1, 7)
dado2 = random.randrange(1, 7)
dado3 = random.randrange(1, 7)
print('Sus dados son: "', dado1, '", "', dado2, '" y "', dado3, '"')
input('Presione enter para continuar')
if dado1 == dado2 and dado1 == dado3:
    puntos2 = 6
    print('Los 3 dados de ', nombre_2, ' son iguales, suma 6 puntos')

# Si el primer y segundo dado son iguales (el tercero es distinto)

elif dado1 == dado2:
    print(dado1, ' y ', dado2, 'Son iguales, deberá relanzar el tercer dado que antes había sido de ', dado3,
          'y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado3 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado3)
    if dado1 == dado3:
        puntos2 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado3, 'así que gana tan solo 3 puntos')
        puntos2 = 3

# Si el primer y tercer dado son iguales (el segundo es distinto)

elif dado1 == dado3:
    print(dado1, ' y ', dado3, 'Son iguales, deberá relanzar el segundo dado que antes había sido de ', dado2,
          'y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado2 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado2)
    if dado1 == dado2:
        puntos2 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado2, 'así que gana tan solo 3 puntos')
        puntos2 = 3

# Si el segundo y tercer dado son iguales (el primero es distinto)

elif dado2 == dado3:
    print(dado2, ' y ', dado3, 'Son iguales, deberá relanzar el primer dado que antes había sido de ', dado1,
          'y si sale igual a los anteriores, suma 6 puntos, de lo contrario suma 3')
    input('Presione enter para lanzar')
    dado1 = random.randrange(1, 7)
    print('Su dado relanzado es :', dado1)
    if dado1 == dado2:
        puntos2 = 6
        print('Al ser los 3 dados iguales, suma 6 puntos')
    else:
        print('Su dado relanzado fue de ', dado1, 'así que gana tan solo 3 puntos')
        puntos2 = 3

# Si ningún dado es igual, todos distintos

else:
    print('Todos los dados son distintos, así que no sumó ningún punto')
    puntos2 = 0

print('\n ', nombre_1, ' consiguió ', puntos1, ' puntos\n', nombre_2, 'consiguió', puntos2, ' puntos.')
print('*****************************')
input('Presione enter para continuar')

# Ronda 2, empieza el jugador 1

print('\nComienza la ronda 2, cada jugador deberá volver a lanzar y adivinar si la suma de sus dados dará par o impar')
print('\n', nombre_1, ' a continuación, elija escribiendo las palabras "par" o "impar"')
decision = input('*** ojo ***Escriba "par" o impar": ')
dado1 = random.randrange(1, 7)
dado2 = random.randrange(1, 7)
dado3 = random.randrange(1, 7)
sumadados1 = dado1 + dado2 + dado3

# Si escribió "par"

if len(decision) == 3:
    input('Eligió "par". Presione enter para tirar los dados')
    print('Sus dados son "', dado1, '",', dado2, '" y "', dado3, '" y la suma de ellos es de ', sumadados1)
    input('Presione enter para continuar\n')
    if sumadados1 % 2 == 0:
        may = max(dado1, dado2, dado3)
        puntos1 = puntos1 + may
        print('\nFelicitaciones! La suma fue par asi que se le suma el valor del dado mas grande,', may,
              'a su puntaje anterior')
        print('Su puntaje es de:', puntos1)
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            print('********************************')
            print('Además, al ser los tres dados pares, se duplica su puntaje!!')
            puntos1 *= 2
            print('Por lo tanto, su puntaje final es de: ', puntos1)
    else:
        men = min(dado1, dado2, dado3)
        puntos1 = puntos1 - men
        print('Lo siento! La suma de los dados fue impar asi que se le resta el valor del dado menor, ', men,
              ' a su puntaje anterior')
        print('Su puntaje final es de: ', puntos1)

# Si escribió "impar" u otra cosa distinta de "par"

else:
    if len(decision) != 5:
        print('Escribió mal "par" o "impar" así que se le asignó "impar" por defecto.')
    input('Eligió "impar". Presione enter para tirar los dados')
    print('Sus dados son "', dado1, '",', dado2, '" y "', dado3, '" y la suma de ellos es de ', sumadados1)
    input('Presione enter para continuar\n')
    if sumadados1 % 2 != 0:
        may = max(dado1, dado2, dado3)
        puntos1 = puntos1 + may
        print('\nFelicitaciones! La suma fue impar asi que se le suma el valor del dado mas grande,', may,
              'a su puntaje anterior')
        print('Su puntaje es de: ', puntos1)
        if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
            print('********************************')
            print('Además, al ser los tres dados de la paridad elegida, se duplica su puntaje!!')
            puntos1 *= 2
            print('Por lo tanto, su puntaje final es de: ', puntos1)
    else:
        men = min(dado1, dado2, dado3)
        puntos1 = puntos1 - men
        print('Lo siento! La suma de los dados fue impar asi que se le resta el valor del dado menor, ', men,
              ' a su puntaje anterior')
        print('Su puntaje final es de: ', puntos1)

# Ronda 2, Jugador 2

print('\n', nombre_2, ' preparate para jugar')
decision = input('*** ojo ***Escriba "par" o impar": ')
dado1 = random.randrange(1, 7)
dado2 = random.randrange(1, 7)
dado3 = random.randrange(1, 7)
sumadados1 = dado1 + dado2 + dado3

# Si eligió "par"

if len(decision) == 3:
    input('Eligió "par". Presione enter para tirar los dados')
    print('Sus dados son "', dado1, '",', dado2, '" y "', dado3, '" y la suma de ellos es de ', sumadados1)
    input('Presione enter para continuar\n')
    if sumadados1 % 2 == 0:
        may = max(dado1, dado2, dado3)
        puntos2 = puntos2 + may
        print('\nFelicitaciones! La suma fue par asi que se le suma el valor del dado mas grande,', may,
              'a su puntaje anterior')
        print('Su puntaje es de: ', puntos2)
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            print('********************************')
            print('Al ser los tres dados de la paridad elegida, se duplica su puntaje!!')
            puntos2 *= 2
            print('Su puntaje final es de: ', puntos2)
    else:
        men = min(dado1, dado2, dado3)
        puntos2 = puntos2 - men
        print('Lo siento! La suma de los dados fue impar asi que se le resta el valor del dado menor, ', men,
              ' a su puntaje anterior')
        print('Su puntaje final es de:', puntos2)

# Si escribió "impar" u otra cosa distinta de "par"

else:
    if len(decision) != 5:
        print('Escribió mal "par" o "impar" así que se le asignó "impar" por defecto.')
    input('Eligió "impar". Presione enter para tirar los dados')
    print('Sus dados son "', dado1, '",', dado2, '" y "', dado3, '" y la suma de ellos es de ', sumadados1)
    input('Presione enter para continuar\n')
    if sumadados1 % 2 != 0:
        may = max(dado1, dado2, dado3)
        puntos2 = puntos2 + may
        print('\nFelicitaciones! La suma fue impar asi que se le suma el valor del dado mas grande,', may,
              'a su puntaje anterior')
        print('Su puntaje es de: ', puntos2)
        if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
            print('Al ser los tres dados de la paridad elegida, se duplica su puntaje!!')
            puntos2 *= 2
            print('Su puntaje final es de: ', puntos2)
    else:
        men = min(dado1, dado2, dado3)
        puntos2 = puntos2 - men
        print('Lo siento! La suma de los dados fue impar asi que se le resta el valor del dado menor, ', men,
              ' a su puntaje anterior')
        print('Su puntaje final es de:', puntos2)

# Final

mensajes_finales = 'humillando a su adversario!', 'de taquito', 'con facilidad', 'gloriosamente'

print('\nLos resultados finales son: ')
print(nombre_1, ' ha obtenido ', puntos1)
print(nombre_2, ' ha obtenido ', puntos2)
if puntos1 == puntos2:
    print('Empate, todos pierden!')
elif puntos1 > puntos2:
    print(nombre_1, ' ha ganado ', random.choice(mensajes_finales))
else:
    print(nombre_2, ' ha ganado ', random.choice(mensajes_finales))
