from registro_Alumnos import *


def chequear_vector(vector):
    if len(vector) == 0:
        print('Primero debe cargar alumnos!!')
        return False
    else:
        return True


def validar_entre(lim_inferior, lim_superior, z):
    if z < lim_inferior or z > lim_superior:
        return False

    else:
        return True


def validate(inf, message):
    n = inf

    while n <= inf:
        n = int(input(message))
        if n <= inf:
            print(f'El numero debe ser mayor a {inf}')

    return n


def bubble_sort_por_apellido(v):
    n = len(v)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if v[j].apellido > v[j + 1].apellido:
                ordenado = False
                v[j], v[j + 1] = v[j + 1], v[j]
        if ordenado:
            break


def contar_alumnos_por_nivel(vec):
    contadores = [0] * 12

    for i in range(len(vec)):
        contadores[vec[i].nivel - 1] += 1

    return contadores


def mostrar_contadores(vec):
    print('-- Cantidad de alumnos por nivel -- ')
    for i in range(len(vec)):
        if vec[i] != 0:
            print(f'Nivel {i + 1}: {vec[i]} alumnos.')


def sumar_cuota(vec, dni):
    cuota_sumada = 0
    tutor = buscar_por_dni(vec, dni)

    if tutor is False:
        print('No se encontró ese tutor!')
        return False

    for i in range(len(vec)):
        if vec[i].dni_tutor == tutor.dni_tutor:
            cuota_sumada += vec[i].cuota

    return cuota_sumada


def buscar_por_apellido(vector, apellido):

    for i in range(len(vector)):
        if apellido == vector[i].apellido:
            return vector[i]

    return False


def buscar_por_dni(vector, dni):

    for i in range(len(vector)):
        if dni == vector[i].dni_tutor:
            return vector[i]

    return False


def descontar_porcentaje(vec, apellido, porcentaje):
    apellido = buscar_por_apellido(vec, apellido)

    if apellido is False:
        print('No se encontró el alumno')
        return False

    else:
        for i in range(len(vec)):
            if vec[i].apellido == apellido.apellido:
                descuento = vec[i].cuota * (porcentaje / 100)
                vec[i].cuota = vec[i].cuota - descuento

    return apellido
