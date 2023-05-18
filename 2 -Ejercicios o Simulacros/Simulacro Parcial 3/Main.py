"""
Criterios generales de evaluación:
a.)	Desarrollo del programa completo, incluyendo el menú correctamente planteado, funciones correctamente diseñadas y
parametrizadas (cuando sea apropiado) y validaciones:  [máximo: 3 puntos (20% del puntaje)]
b.)	Desarrollo correcto del ítem 1: [máximo: 3 puntos (20% del puntaje)]
c.)	Desarrollo correcto del ítem 2: [máximo: 3 puntos (20% del puntaje)]
d.)	Desarrollo correcto del ítem 3: [máximo: 3 puntos (20% del puntaje)]
e.)	Desarrollo correcto del ítem 4: [máximo: 3 puntos (20% del puntaje)]
f.)	Para aprobar el parcial, el alumno debe llegar a un total acumulado de al menos 55% del puntaje
(es decir, alrededor de 8.25 puntos acumulados), pero obligatoriamente debe estar desarrollado el programa
con al menos 2 módulos, y modularización en funciones, funcionando y operativo.


Enunciado:
Una academia de inglés para niños de escolaridad primaria y nivel inicial, desea un programa para procesar los
datos de sus alumnos. Por cada alumno se tienen los siguientes datos: DNI del alumno, el nombre del alumno,
el apellido del alumno, DNI del Tutor (adulto responsable del niño), el importe de la cuota y
el nivel en el que cursa el niño
(un valor entre 1 y 12 incluidos, de la forma 1: Inicial, 2: Primer Junior, 3: Primer Younger, etc.).
Se desea almacenar la información referida a los n alumnos en un arreglo de registros de tipo Alumno
(definir el tipo Alumno y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1-	Cargar el arreglo pedido con los datos de los n alumnos. Valide que el número de nivel sea un valor entre 0 y 12
(ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática
(con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2-	Mostrar todos los datos de todos los alumnos, en un listado ordenado de menor a mayor según el apellido del alumno.

3-	Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel
(o sea, 12 contadores). Muestre sólo los resultados diferentes de 0.

4-	Determinar el monto total que debe abonar el Tutor con número de DNI igual a x, siendo x un valor que se carga por
teclado (sumar los importes de las cuotas de los niños que el Tutor tiene a su cargo).

5-	Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda,
debe mostrar sólo el primero que encuentre.
"""

from registro_Alumnos import *


def menu_de_opciones():
    print('-- Menú de opciones -- \n'
          '1- Generar datos de aleatoriamente. \n'
          '2- Cargar datos de alumnos manualmente. \n'
          '3- Mostrar los alumnos cargados, por orden de apellido \n'
          '4- Contar la cantidad de alumnos que cursan en cada nivel. \n'
          '5- Determinar el monto que debe abonar un tutor cargado por teclado. \n'
          '6- Descontarle a un alumno un 10% de su cuota y mostrar sus datos. \n'
          '7- Salir')

    op = int(input('Ingrese una opción: '))

    return op


def Main():
    op = 0
    alumnos = []

    while op != 7:
        op = menu_de_opciones()

        if op == 1:
            n = validate(0, 'Cuantos alumnos quiere generar?: ')

            for i in range(n):
                alumnos.append(generate_alumno())

            bubble_sort_por_apellido(alumnos)

        if op == 2:
            n = validate(0, 'Cuantos alumnos desea cargar?: ')

            for i in range(n):
                alumnos.append(cargar_alumno())

            bubble_sort_por_apellido(alumnos)

        if op == 3:
            if not chequear_vector(alumnos):
                continue

            for i in range(len(alumnos)):
                print(alumnos[i])

        if op == 4:
            if not chequear_vector(alumnos):
                continue

            contadores = contar_alumnos_por_nivel(alumnos)
            mostrar_contadores(contadores)

        if op == 5:
            if not chequear_vector(alumnos):
                continue

            dni = int(input('Que DNI desea buscar? '))
            cuota = sumar_cuota(alumnos, dni)

            if not cuota:
                continue
            else:
                print(f'El tutor debe pagar {cuota}')

        if op == 6:
            if not chequear_vector(alumnos):
                continue
            apellido = input('De que apellido desea descontar 10%?: ')

            if apellido is False:
                continue
            else:
                alumno = descontar_porcentaje(alumnos, apellido, 10)
                print(alumno)

    print('chau!')


if __name__ == '__main__':
    Main()
