import pickle
import os
from registro_Servicio import *

formas_de_pago = ('Efectivo', 'Crédito', 'Débito', 'Transferencia', 'Fiado')


def menu_de_opciones():

    print('-' * 10)
    print('MENU DE OPCIONES')
    print('-' * 10)
    print('1 -> Agregar n datos al vector, generados automáticamente \n'
          '2 -> Mostrar los valores en el vector, de un tipo mayor a un número específico \n'
          '3 -> Mostrar la cantidad de servicios de cada posible tipo por cada posible forma de pago \n'
          '4 -> Crear un archivo con servicios cuyo importe sea mayor a un número\n'
          '5 -> Mostrar un arhivo\n'
          '6 -> Salir')

    op = validar_entre('Ingrese una opción: ', 1, 6)

    return op


def validar_entre(msg, limite_inferior, limite_superior):

    x = int(input(msg))
    while x < limite_inferior or x > limite_superior:
        print(f'El valor deber estar entre {limite_inferior} y {limite_superior}')
        x = int(input('Ingrese un valor válido: '))

    return x


def validar_entero(msg):
    x = int(input(msg))
    while x <= 0:
        x = int(input('Ingrese un número entero: '))

    return x


def add_in_order_id(reg, vec):
    n = len(vec)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].id == reg.id:
            pos = c
            break
        if reg.id < vec[c].id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def generar_vector(x, vec):
    for i in range(x):
        reg = generar_registo()
        add_in_order_id(reg, vec)


def mostrar_vector(vec, x):
    for i in range(len(vec)):
        if vec[i].tipo >= x:
            print(vec[i])


def generar_matriz(vec):
    mat = [[0] * 5 for i in range(25)]

    for i in range(len(vec)):
        fil = vec[i].tipo
        col = vec[i].medio_pago

        mat[fil][col] += 1

    return mat


def mostrar_matriz(vec, d):
    vueltas = 0
    for i in range(len(vec)):
        for j in range(len(vec[i])):
            if vec[i][j] > 0 and vec[i][j] > d:
                vueltas += 1
                print(f'Tipo de servicio: {i} Forma de pago: {formas_de_pago[j]}: Total: {vec[i][j]}')
    if vueltas == 0:
        print('No se han encontrado contadores que cumplan la condición.')


def crear_archivo(nombre, x, vec):
    cant_archivos = 0
    arch = open(nombre, 'wb')
    for i in range(len(vec)):
        if vec[i].importe < x:
            cant_archivos += 1
            pickle.dump(vec[i], arch)
    arch.close()
    print(f'Se ha creado el archivo {nombre} con {cant_archivos} servicios!')


def mostrar_archivo(nombre):
    if not os.path.exists(nombre):
        print('Ese archivo no existe!')
        return

    else:
        suma = 0
        vueltas = 0
        arch = open(nombre, 'rb')
        tam = os.path.getsize(nombre)

        while arch.tell() < tam:
            reg = pickle.load(arch)
            suma += reg.importe
            vueltas += 1
            print(reg)
        arch.close()

        print(f'El promedio de los importes es de: {round(suma / vueltas, 2)}')
