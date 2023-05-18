# Simulacro de parcial

__author__ = 'Federico Wedemeyer, 1K6, 90832'

# Funcion

from Funcion import conversor

#  Banderas
record = False
first = True
op = 0
counter = 0
suma = 0
fastest = 0

# Menu de opciones

while op != 4:

    print('\n~Bienvenido al programa re copado y divertido~')
    print('Elija una opcion')
    print('1- Analizador de temperaturas')
    print('2- Analizador de tiempos de corredores')
    print('3- Navegador de caracteres')
    print('4- Salir')
    op = int(input('Ingrese una opcion: '))

# OPCION 1
    if op == 1:
        place1 = input('Introduzca el nombre del primer lugar: ')
        temp1 = input('Introduzca la temperatura de dicho lugar: ')
        place2 = input('Introduzca el nombre del segundo lugar: ')
        temp2 = input('Introduzca la temperatura de dicho lugar: ')
        place3 = input('Introduzca el nombre  del tercer lugar: ')
        temp3 = input('Introduzca la temperatura de dicho lugar: ')
        lowest = input('Cual fue la menor temperatura registrada? ')
        if temp1 < temp2 and temp1 < temp3:
            tmin = temp1
            min_place = place1
        elif temp2 < temp1 and temp2 < temp3:
            tmin = temp2
            min_place = place2
        else:
            tmin = temp3
            min_place = place3
        if tmin < lowest:
            record = True
        print('La menor temperatura fue en, ', min_place, 'con une temperatura de: ', tmin, '°')
        if record is True:
            print('Fue incluso menor que la anterior temperatura historica de, ', lowest, '°')

# OPCION 2
    elif op == 2:
        n = int(input('Ingrese la cantidad de corredores a evaluar: '))
        usain_bolt = int(input('Cual fue el record anterior, en segundos? '))

        for i in range(n):
            t = float(input('Ingrese el tiempo de un corredor en segundos: '))
            if first is True:
                fastest = t
                first = False
            if fastest > t:
                fastest = t
            counter += t
        h, m, s = conversor(fastest)
        print('El promedio de tiempos fue de', counter/n)
        print('El tiempo mas rapido fue de: ', h, 'hs', m, 'm', s, 's')
        if fastest < usain_bolt:
            print('que fue incluso mas rapido que Usain Bolt, que tenia el anterior record de', usain_bolt)
# OPCION 3
    elif op == 3:
        texto = input('Ingrese un texto: ')
        for letra in texto:
            if letra == '2' or letra == '4' or letra == '6' or letra == '8' or letra == '0':
                suma += int(letra)
        print('La suma de numeros pares es de', suma)

# SI ELIGIO MAL
    else:
        print('Elegi alguna de las opciones, perejil')


print('Gracias por usar el programa re copado y divertido')
