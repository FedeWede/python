"""
Una empresa de alquiler de vehículos necesita un programa para procesar los datos de los alquileres que tiene
ofrecidos.
Por cada alquiler se tienen los siguientes datos:
número de identificación de esa operación,
descripción del automóvil  alquilado,
el tipo de vehículo (un número entero entre 1 y 10, para indicar por ejemplo: 1: sedán cuatro puertas, 2: familiar siete
 asientos, etc.),
el importe a cobrar por el alquiler y
la cantidad de días por los que se hace el alquiler.

Se desea almacenar la información referida a los n alquileres en un arreglo de registros de tipo Alquiler
(definir el tipo Alquiler y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n alquileres. Valide que el número identificador de la operación de
alquiler sea positivo y que el tipo del vehículo esté entre 1 y 10. Puede hacer la carga en forma manual, o puede
generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea.
Pero al menos una debe programar.

2- Mostrar todos los datos de todos los alquileres, en un listado ordenado de menor a mayor según los importes a cobrar
de esos alquileres. En el listado no incluya la visualización de la cantidad de días de alquiler. Al final del listado,
mostrar una línea adicional en la que se indique el importe promedio pagado entre todos los vehículos que se mostraron.

3- Determinar y mostrar la cantidad de alquileres que se hicieron de cada tipo posible de vehículo (un contador para los
alquileres tipo 1, otro para el tipo 2, etc.) En total, 10 contadores. Muestre solo los resultados mayores a cero.

4- Determinar y mostrar el alquiler con mayor importe. Mostrar además la diferencia entre este importe mayor, y el
importe promedio entre todos los alquileres del arreglo.

5- Determinar si fue alquilado un vehículo cuya descripción sea igual a c y que tenga un importe de x o más,
siendo c y x dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
"""

from modulo import *


def mostrar_menu_de_opciones():
    print('---- Bienvenido al gestor de alquileres!! ----\n'
          '1- Generar alquileres automáticamente\n'
          '2- Cargar alquileres manualmente\n'
          '3- Mostrar autos alquilados según importe\n'
          '4- Mostrar la cantidad de alquileres por tipo de vehículo\n'
          '5- Mostrar el alquiler de mayor importe, y la diferencia entre este y el promedio de todos los importes\n'
          '6- Mostrar si fue alquilado un vechículo de una descripción específica con un importe específico\n')


def principal():
    op = 0
    alquileres = []
    while op != 7:
        mostrar_menu_de_opciones()
        op = int(input('Seleccione una opción: '))

        if op == 1:
            n = int(input('Cuantos autos desea generar?: '))
            print('Generando alquileres...')
            carga_automatica(n, alquileres)
            bubble_sort_importe(alquileres)

        if op == 2:
            n = int(input('Cuantos alquileres desea cargar?: '))
            carga_manual(n, alquileres)
            bubble_sort_importe(alquileres)

        if op == 3:
            if len(alquileres) == 0:
                print('No hay autos cargados!! ')
            else:
                mostrar_vector(alquileres)

        if op == 4:
            if len(alquileres) == 0:
                print('No hay autos cargados!! ')
            else:
                contadores = contar_alquileres_por_tipo(alquileres)
                mostrar_contadores(contadores)

        if op == 5:
            if len(alquileres) == 0:
                print('No hay autos cargados!! ')

            else:
                # mayor = alquileres[-1] al tener el vector ordenado de menor a mayor, yo podría acceder al de mayor
                # importe accediendo al último elemento de la lista. No lo dejé porque no sabía si iba a ser contado
                # como una resolución correcta para el parcial, sin embargo lo dejo comentado para mostrar otra
                # solución que encontré, más simple.

                mayor = buscar_mayor_importe(alquileres)
                promedio = calcular_promedio(alquileres)
                print(f'El alquiler de mayor importe es \n'
                      f'{mayor}\n')
                print(f'La diferencia del mayor con el promedio de importes ({promedio}) es de: '
                      f'{mayor.importe - promedio} \n')

        if op == 6:
            if len(alquileres) == 0:
                print('No hay autos cargados!! ')

            else:

                c = input('Que descripción de vehículo desea buscar?: ')
                x = int(input('Que importe deberá tener?: '))

                alquiler = buscar_alquiler(alquileres, c, x)
                if alquiler != -1:
                    print('El alquiler buscado es: \n')
                    print(alquiler)


if __name__ == '__main__':
    principal()