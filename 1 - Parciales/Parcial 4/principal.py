"""
Una empresa de construcción, mantenimiento  y reparaciones mantiene información sobre los distintos servicios que debe
realizar. Por cada servicio se registran los datos siguientes: número de identificación del servicio (un número entero),
descripción del servicio (una cadena), importe a facturar por el servicio, tipo de servicio (un valor entre 0 y 24
incluidos, por ejemplo: 0: pintura, 1: ampliación, etc.) y forma de pago (un número entero entre 0 y 4 incluidos,
para indicar (por ejemplo): 0: contado, 1: tarjeta de crédito, etc.) Se pide definir un tipo registro Servicio con los
campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Servicio en un arreglo de registros (cargue n por teclado). Valide los campos
que sea necesario. Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual,
TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática).  El arreglo debe crearse de
forma que siempre quede ordenado de menor a mayor, según el número de identificación de los servicios y para hacer esto
debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada
pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea, pero muestre solo los registros cuyo
tipo de servicio sea mayor o igual al valor tipo que se carga por teclado.

3- Usando el arreglo creado en el punto 1, determine la cantidad de servicios de cada posible tipo por cada posible
forma pago (o sea, 25 * 5 contadores en una matriz de conteo). Muestre solo los resultados que sean diferentes de cero
pero mayores que un valor d que se carga por teclado.

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los servicios cuyo
importe a facturar sea menor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla. Agregar al final del
listado una línea adicional, que indique el promedio de los importes a facturar de todos los registros que se mostraron.


"""

from modulo import *


def Principal():
    op = 0
    vec_servicios = []

    while op != 6:
        op = menu_de_opciones()

        if op == 1:
            n = validar_entero('\nCuantos servicios desea agregar?: ')
            generar_vector(n, vec_servicios)
            print('Vector generado con éxito!')
            input('Presione enter para continuar...')

        if op == 2:
            if len(vec_servicios) == 0:
                print('\nNo ha generado el vector con servicios!')
                input('Presione enter para continuar... ')
            else:
                num = validar_entre('\nMostrar solo los servicios de tipo igual o mayor al número: ', 0, 24)
                mostrar_vector(vec_servicios, num)
                input('Presione enter para continuar...')

        if op == 3:
            if len(vec_servicios) == 0:
                print('\nNo ha generado el vector con servicios!')
                input('Presione enter para continuar... ')

            else:
                d = validar_entero('\nContadores mayores a qué número desea ver?: ')
                mat = generar_matriz(vec_servicios)
                mostrar_matriz(mat, d)

        if op == 4:
            if len(vec_servicios) == 0:
                print('\nNo ha generado el vector con servicios!')
                input('Presione enter para continuar... ')

            else:
                nombre = input('\nQue nombre desea ponerle al archivo?: ')
                if os.path.exists(nombre):
                    print('Ese archivo ya existe.')
                else:
                    x = validar_entero('\nA que importe deberán ser menores los servicios cargados?: ')
                    crear_archivo(nombre, x, vec_servicios)

        if op == 5:
            nombre = input('\nQue archivo desea ver?: ')
            mostrar_archivo(nombre)

    print('Adios!')


if __name__ == '__main__':
    Principal()
