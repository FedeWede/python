
# Establecer el tamano del mapa.
import random

x_largo = int(input('Ingrese el largo del mapa: '))
y_alto = int(input('Ingrese el alto del mapa: '))
while x_largo > 800 or x_largo < 100 or y_alto > 800 or y_alto < 100:
    print('Ingreso datos incorrectos. El largo y alto minimo del mapa es 800 y el maximo es 800')
    x_largo = int(input('Ingrese el largo del mapa: '))
    y_alto = int(input('Ingrese el alto del mapa: '))

# Posicion de Tito
pos_x = random.randint(1, x_largo)
pos_y = random.randint(1, y_alto)
print('**************************************************************************\n'
      'Actualmente Tito spawneo en', pos_x, ';', pos_y,  '\n')

# Menu de opciones
acumulador = 0
opc = None
while opc != 6:
    opc = int(input('''**************************************************************************
    Tito puede moverse al norte, sur, este u o este. Tambien puede ver cuanto se movio Tito
    1- Moverse hacia el norte
    2- Moverse hacia el sur
    3- Moverse hacia el este
    4- Moverse hacia el oeste
    5- Ver estadisticas
    6- Salir del juego
    Ingrese su decision: '''))

    # Lo mueven al norte

    if opc == 1:
        movn = int(input('Cuanto quiere mover a Tito hacia el Norte?:  '))
        pos_y += movn
        if pos_y > y_alto:
            pos_y -= movn
            acumulador += y_alto - pos_y
            print('Tito no puede moverse ahi porque se caeria de la faz de la tierra plana')
            pos_y = y_alto
            print('**************************************************************************\n'
                  'Tito se movio', movn, ' pasos al Norte y ahora se encuentra en: ', pos_x, ':', pos_y)
        else:
            print('**************************************************************************\n'
                  'Tito se movio', movn, ' pasos al Norte y ahora se encuentra en: ', pos_x, ':', pos_y)
            acumulador += movn

    # Lo mueven al sur

    elif opc == 2:
        movs = int(input('Cuanto quiere mover a Tito hacia el Sur?:  '))
        pos_y -= movs
        if pos_y < y_alto:
            pos_y += movs
            acumulador += pos_y
            print('Tito no puede moverse ahi porque se caeria de la faz de la tierra plana')
            pos_y = 0
            print('**************************************************************************\n'
                  'Tito se movio', movs, ' pasos al Sur y ahora se encuentra en: ', pos_x, ':', pos_y)
        else:
            print('**************************************************************************\n'
                  'Tito se movio', movs, ' pasos al Sur y ahora se encuentra en: ', pos_x, ':', pos_y)
            acumulador += movs

    # Lo mueven al este

    elif opc == 3:
        move = int(input('Cuanto quiere mover a Tito hacia el Este?:  '))
        pos_x += move
        if pos_x > x_largo:
            pos_x -= move
            acumulador += x_largo - pos_x
            print('Tito no puede moverse ahi porque se caeria de la faz de la tierra plana')
            pos_x = x_largo
            print('**************************************************************************\n'
                  'Tito se movio', move, ' pasos al Este y ahora se encuentra en: ', pos_x, ':', pos_y)
        else:
            print('**************************************************************************\n'
                  'Tito se movio', move, ' pasos al Este y ahora se encuentra en: ', pos_x, ':', pos_y)
            acumulador += move

    # Lo mueven al oeste
    elif opc == 4:
        movo = int(input('Cuanto quiere mover a Tito hacia el Oeste:  '))
        pos_x -= movo
        if pos_x <= x_largo:
            pos_x += movo
            acumulador += pos_x
            print('Tito no puede moverse ahi porque se caeria de la faz de la tierra plana')
            pos_x = 0
            print('**************************************************************************\n'
                  'Tito se movio', movo, ' pasos al Oeste y ahora se encuentra en: ', pos_x, ':', pos_y)
        else:
            print('**************************************************************************\n'
                  'Tito se movio', movo, ' pasos al Oeste y ahora se encuentra en: ', pos_x, ':', pos_y)
            acumulador += movo
    elif opc == 5:
        print('Tito se ha movido un total de: ', acumulador, 'unidades de mapa')
    else:
        print('Perejil, tenes que elegir uno de los numero de las opciones')
print('Gracias por jugar!')
