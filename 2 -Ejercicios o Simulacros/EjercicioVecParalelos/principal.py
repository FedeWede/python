__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import validaciones

'''
Ejercicio
=========

Considere el siguiente código incompleto, el mismo posee un menú de opciones que permite cargar un conjunto de datos con 
información de los archivos que contienen la estructura de procesos a ejecutar para crear una base de datos.
De dichos archivos se conoce 
    el nombre (una cadena de 8 letras más .txt que debe ser validado que cumpla estas condiciones), 
    el contenido codificado 
    (una cadena que puede incluir las letras: e - estructura | p - procedimientos | f - funciones | d - datos; 
        la cadena puede incluir todas las letras por ejemplo "epfd" o solo algunas por ejemplo "ed" se debe validar que 
        al menos inlcuya una letra y que no pueda incluir ninguna de letra distinta a estas 4)
    la cantidad de filas de datos que agrega (un número entero)   

El programa ya contiene una funcionalidad para generar datos aleatorios, y una funcionalidad para mostrar todos datos de 
todas las entradas.

Su trabajo consiste en completar el código de las funciones para realizar lo que cada opción de menú promete. Revise
el comentario de cada función para obtener más detalle.
'''

from validaciones import *
import random


def mostrar_menu():
    """
    Función que genera el menú y retorna la opción elegida (y validada).

    :return op: Opción elegida por el usuario
    """
    menu = '\n1) Agregar un archivo' \
           '\n2) Generar datos aleatorios' \
           '\n3) Mostrar Valores' \
           '\n4) Mostrar el o los archivos con mayor cantidad de filas' \
           '\n5) Validar nombres' \
           '\n6) Buscar valor (Búsqueda secuencial)' \
           '\n7) Buscar valor (Búsqueda binaria)' \
           '\n8) Buscar un archivo por nombre y permitir modificar sus datos'  \
           '\n9) Salir' \
           '\n' \
           '\nIngrese una opción: ' \


    op = validar_entre(1,9,menu,'Opción inválida')
    return op


def generar_cadena_contenido():
    cadenas = ('epfd', 'epf', 'efd', 'ed', 'e', 'd', 'pf', 'p', 'f')

    res = random.choice(cadenas)

    return res;

def generar_cadena_nombre():

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = ""

    for i in range(8):
        res += random.choice(letras)

    res += '.txt'

    return res;



def generar_valores():
    """
    Genera valores aleatorios entre 0 y 500.

    :return nom: El vector con los nombres.
    :return con: El vector con los contenidos.
    :return can: El vector con las cantidades.
    """
    n = validar_mayor_igual(1,'Ingrese la cantidad de elementos: ')
    nom = []
    con = []
    can = []

    for i in range(n):
        nom.append(generar_cadena_nombre())
        c = generar_cadena_contenido()
        con.append(c)
        if 'd' in c:
            can.append(random.randint(1,500))
        else:
            can.append(0)

    return nom, con, can


def mostrar_valores(nombre, contenido, cantidad):
    print('Listado de archivos: ')
    print('Nombre\t\t\tCont\tCantidad')
    print('------\t\t\t----\t--------')

    for i in range(len(nombre)):
        print(nombre[i], end='')
        print('\t', end='')
        print(contenido[i], end='')
        print('\t\t', end='')
        print(cantidad[i])

    print()


def buscar_mayores(cantidad):
    """
    Función que toma por parámetro el vector de las cantidades y retorna otro venctor con los índices de las posiciones
    con el mayor valor, puede ser un solo índice si son todos distintos o todos los índices si todos los valores fueran iguales
    o cualquier número entre 1 y todos.

    :param cantidad: El vector con las cantidades
    :return mayores: El vector con los índices de los mayores
    """
    pass


def validar_nombres(valores):
    """
    Función que valida que no haya valores repetidos en el vector.

    :param valores: El vector con los datos a validar
    :return válido: Verdadero si NO hay valores repetidos y Falso en caso contrario
    """
    pass


def contar_primos(valores):
    """
    Función que indica la cantidad de números primos que existen en el arreglo.
    Tenga en consideración que un número primo es aquel que solo puede ser dividido exactamente por si mismo y por la
    unidad. NO considere al 1 como primo, llegado el caso.

    :param valores: El vector con los datos
    :return cantidad_primos: La cantidad de números primos encontrados
    """
    pass


def busqueda_secuencial(x, valores):
    """
    Función que realiza una búsqueda secuencial del valor x, sobre el arreglo valores.

    :param x: El valor a buscar
    :param valores: El vector con los valores generados
    :return indice: El índice donde se encontró el valor o -1 en caso contrario
    """
    pass


def busqueda_binaria(x, valores):
    """
    Función que realiza una búsqueda binaria del valor x, sobre el arreglo de valores.
    OJO!, recuerde las precondiciones para una búsqueda binaria.

    :param x: El valor a buscar
    :param valores: El vector de datos generados
    :return indice: El índice donde se encontró el valor o -1 en caso contrario
    """
    pass


def agregar_uno(nombre, contenido, cantidad):
    """
    Función que realiza la carga de los 3 datos de un archivo y los argrega a los vectores.
    Recuerde que debe validar que el nombre tenga 8 letras + '.txt', y que sea único en el conjunto de nombres existente
    , y que el contenido tenga al menos una letra y no incluya ninguna letra distinta de 'e', 'p', 'f' o 'd' ni tampoco
    letras repetidas

    :param nombre: El vector de nombres de archivos
    :param contenido: El vector de contenidos
    :param cantidad: El vector de cantidades
    """

    name = validaciones.validar_nombres()
    nombre.append(name)

    cont = validaciones.validar_contenido()
    contenido.append(cont)

    cant = int(input('Ingrese la cantidad de datos: '))
    cantidad.append(cant)


def principal():
    """ Función principal """
    nombre = []
    contenido = []
    cantidad = []

    op = -1
    while op != 9:
        # Se muestra el menú, en una función separada así el código es más legible
        op = mostrar_menu()
        # Si se requiere una opción que utiliza los valores y los mismos aún no se cargaron
        # Se indica la situación y se continúa
        if op != 1 and op != 2 and op != 9 and len(nombre) == 0:
            print("Debe cargar los valores primero")
            continue

        if op == 1:# Agregar un archivo

            agregar_uno(nombre, contenido, cantidad)

        elif op == 2: #Generar datos aleatorios
            nombre, contenido, cantidad = generar_valores()
            mostrar_valores(nombre, contenido, cantidad)

        elif op == 3:# Opción 3, Mostrar los valores
            mostrar_valores(nombre, contenido, cantidad)

        elif op == 4:# Opción 4, Mostrar el o los archivos con mayor cantidad de filas
            # mayores es un vector porque puede haber más de un archivo con la misma mayor cantidad de filas

            mayores = buscar_mayores(cantidad)
            print('El/Los archivo/s con mayor cantidad de filas son: ')
            for i in range(len(mayores)):
                print(nombre[mayores[i]], end='')
                print('\t', end='')
                print(contenido[mayores[i]], end='')
                print('\t\t', end='')
                print(cantidad[mayores[i]])

        elif op == 5:# Opción 5, Validar nombres

            if validar_nombres(nombre):
                print("Los datos son consistentes, no hay nombres repetidos.")
            else:
                print("Los datos están inconsistentes, hay nombres repetidos")

        elif op == 6:# Opción 6, Búsqueda SECUENCIAL
            x = input("Ingrese el nombre a buscar: ")
            indice = busqueda_secuencial(x, nombre)
            if indice == -1:
                print("El valor " + x + "NO se encontró")
            else:
                print("El valor " + x + " se encontró:")
                print(nombre[indice], end='')
                print('\t', end='')
                print(contenido[indice], end='')
                print('\t\t', end='')
                print(cantidad[indice])

        elif op == 7:# Opción 7, Búsqueda BINARIA
            x = input("Ingrese el nombre a buscar: ")
            indice = busqueda_binaria(x, nombre, contenido, cantidad)
            if indice == -1:
                print("El valor " + x + "NO se encontró")
            else:
                print("El valor " + x + " se encontró:")
                print(nombre[indice], end='')
                print('\t', end='')
                print(contenido[indice], end='')
                print('\t\t', end='')
                print(cantidad[indice])
        elif op == 8:# Opción 8, Buscar y Modificar
            # Este queda completamente liberado a vuestra implementación
            print ('Aún no implementado')
        elif op == 9:# Opción 9, Salir del programa
            print("Hasta Luego!")


if __name__ == '__main__':
    principal()
