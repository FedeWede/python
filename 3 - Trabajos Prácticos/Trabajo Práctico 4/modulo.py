import os
import pickle
from registro_Libro import *


def menu_de_opciones():
    print('\n', '-' * 20)
    print('GESTOR DE LIBROS 2.O')
    print('-' * 20)
    print('1 -> Cargar el archivo "libros.csv"\n'
          '2 -> Sumar revisión a un libro buscado por ISBN o título\n'
          '3 -> Buscar el libro con más revisiones\n'
          '4 -> Generar matriz con los libros entre 2000-2020 con mayor rating de cada año, por cada idioma\n'
          '5 -> Mostrar la cantidad de libros por década\n'
          '6 -> Generar un archivo con los libros más populares\n'
          '7 -> Mostrar archivo de libros populares\n'
          '8 -> Salir')


def validar_entre(msg, limite_superior, limite_inferior=0):  # para validar que un número esté dentro de un rango
    x = int(input(msg))
    while x < limite_inferior or x > limite_superior:
        print('El valor deber estar entre', limite_inferior,
              'y', limite_superior)
        x = int(input(msg))
    return x


# Ejercicio 1 - Abajo de este comentario están las funciones necesarias para el Ej 1.
def separador_cadenas(texto, separador):  # para separar una cadena separada por un carácter, entre varias
    cadenas = []
    cadena_actual = ''

    for car in texto:
        if car != separador:
            cadena_actual += car
        else:
            cadenas.append(cadena_actual)
            cadena_actual = ''

    if texto[-1] != separador:
        cadenas.append(cadena_actual)

    return cadenas


def add_in_order_isbn(reg, vec):  # agregar según mayor a menor ISBN a un vector
    n = len(vec)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].isbn == reg.isbn:
            pos = c
            break
        if reg.isbn < vec[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def procesar_archivo():  # cargar un archivo de texto línea por línea a un vector, de manera que quede ordenado y
    # separado en registros

    libros = []
    vuelta = 0
    m = open("libros.csv", mode="rt", encoding="utf8")

    for linea in m:
        vuelta += 1

        if vuelta > 1:
            if linea[-1] == '\n':
                linea = linea[:-1]

            cadena = separador_cadenas(linea, separador=',')

            reg = Libro(cadena[0], cadena[1], cadena[2], cadena[3], cadena[4], cadena[5])

            add_in_order_isbn(reg, libros)

    m.close()
    print(f'\nSe han cargado {vuelta - 1} libros')
    return libros


def mostrar_vector(vec):  # mostrar un vector en pantalla
    for i in range(len(vec)):
        print(vec[i])


# Ejercicio 2 - Abajo de este comentario están las funciones necesarias para el Ej 2.
def binary_search_isbn(vec, busqueda):  # busqueda binaria por ISBN
    n = len(vec)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if busqueda == vec[c].isbn:
            return c
        if busqueda < vec[c].isbn:
            der = c - 1
        else:
            izq = c + 1
    return False


def linear_search_titulo(vec, x):  # busqueda lineal por título
    for i in range(len(vec)):
        if x == vec[i].titulo.lower():
            return i
    return False


def sumar_revision_isbn(vec):  # sub-problema del ejercicio 2, cuando un libro quiere ser buscado por isbn
    busqueda = input("Ingrese el numero de ISBN de 11 elementos que quiere buscar: ")

    pos = binary_search_isbn(vec, busqueda)
    if not pos:
        print('Ese libro no existe!')
        return
    else:
        vec[pos].cant_rev += 1
        print(f'Se ha sumado una revisión a:\n'
              f'{vec[pos]}')
        print(f'Antes tenía {vec[pos].cant_rev - 1} revisiones')


def sumar_revision_titulo(vec):  # sub-problema del ejercicio 2, cuando un libro quiere ser buscado por titulo
    busqueda = input("Ingrese el titulo que quiere buscar: ").lower()
    pos = linear_search_titulo(vec, busqueda)

    if not pos:
        print('Ese libro no existe!')
    else:
        vec[pos].cant_rev += 1
        print(f'Se ha agregado una revisión a:\n'
              f'{vec[pos]}')
        print(f'Antes tenía {vec[pos].cant_rev - 1}')


def sumar_revision(vec):
    print('\n\n', '-' * 20)
    print(f'Aquí podrá buscar un libro por su ISBN o por su TITULO\n'
          f'Luego se mostrarán sus datos en el caso de que exista y se sumara una revision al mismo.\n'
          f'En el caso de que no exista, se avisará mediante un mensaje.\n'
          f'Para la busqueda ingrese 1. ISBN o 2. Titulo')
    op_busqueda = validar_entre('--> ', 2, 1)

    if op_busqueda == 1:
        sumar_revision_isbn(vec)

    if op_busqueda == 2:
        sumar_revision_titulo(vec)


# Ejercicio 3 - Abajo de este comentario están las funciones necesarias para el Ej 3.
def buscar_mayor_revisiones(vec):
    mayor = vec[0]
    for i in range(len(vec)):
        if vec[i].cant_rev > mayor.cant_rev:
            mayor = vec[i]
    return mayor


def calcular_promedio_idioma(vec, idioma):
    suma = 0
    vueltas = 0
    for i in range(len(vec)):
        if vec[i].idioma == idioma:
            suma += vec[i].rating
            vueltas += 1
    promedio = round(suma / vueltas, 2)

    return promedio


def ejercicio_3(libro, promedio):
    if round(libro.rating, 2) == promedio:
        print(f'El libro tiene igual rating al promedio de su idioma!\n')
    elif round(libro.rating, 2) > promedio:
        print(f'El libro tiene mayor rating al promedio de su idioma!\n')
    else:
        print('El libro tiene menor rating al promedio de su idioma :(')

    print(f'Rating del libro: {libro.rating} | Promedio del idioma: {promedio}')
    print(libro)


# Ejercicio 4 - Abajo de este comentario están las funciones necesarias para el Ej 4.
def llenar_matriz(v):  # sub-problema del ejercicio 4, llenar la matriz con los datos

    mat = [[0] * 21 for i in range(27)]
    for i in range(len(v)):
        if v[i].anio in range(2000, 2021):
            fila = v[i].idioma - 1
            columna = v[i].anio - 2000

            if mat[fila][columna] != 0:
                if mat[fila][columna].rating < v[i].rating:
                    mat[fila][columna] = v[i]
            else:
                mat[fila][columna] = v[i]

    print('\nMatriz generada exitosamente')
    return mat


def mostrar_matriz(matriz):  # Ejercicio 4, generar la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                continue
            else:
                print(f'Año: {j + 2000} | Idioma {i + 1} Cantidad: {matriz[i][j]}')


# Ejercicio 5 - Abajo de este comentario están las funciones necessarias para el Ej 5.
def mostrar_decadas(v):
    v2 = [0] * 10
    for i in v:
        if i.anio in range(1900, 2000):
            v2[(i.anio % 100) // 10] += 1

    may_values = [0]
    may_decades = ["00's"]

    for i in range(len(v2)):
        if v2[i] != 0:
            a = str(i) + "0's"
            print(f'{a}: {v2[i]}')

            if i != 0:
                if may_values[0] == v2[i]:
                    may_values.append(v2[i])
                    may_decades.append(a)

                elif may_values[0] < v2[i]:
                    del may_values
                    del may_decades
                    may_values = [v2[i]]
                    may_decades = [a]

    print('\n Décadas más populares: ', end='')

    for i in may_decades:
        print(f'{i}')


# Ejercicio 6 - Abajo de este comentario están las funciones necessarias para el Ej 6.
def generar_archivo(matriz):
    cont = 0
    m = open('populares.dat', 'wb')
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] != 0:
                pickle.dump(matriz[f][c], m)
                cont += 1

    print(f'Fueron agregados {cont} libros')


def leer_archivo():
    if not os.path.exists('populares.dat'):
        print('No existe el archivo')
        return

    m = open('populares.dat', 'rb')
    tamano = os.path.getsize('populares.dat')
    while m.tell() < tamano:
        x = pickle.load(m)
        print(x)
    m.close()
