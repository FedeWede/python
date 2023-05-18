"""
Un colegio secundario de la ciudad está organizando las actividades recreativas de la vuelta a la presencialidad.
Tiene pensado organizar una semana de actividades deportivas y requiere un software para gestionar las inscripciones de
alumnos en los diferentes deportes.
Para ello requiere cargar los datos de los alumnos, de cada alumno se conoce el legajo (un numero entero), el nombre,
el año que cursa (un número entre 1 y 7), y codigo de 0 a 9 que indica el deporte al que se inscribe (0 - basquet, 1 -
rugby seven, 2 - tenis, etc.)
Conociendo esta información se pide un programa con menú de opciones que permita:
Parcial 2:
1 - Cargar los datos de los estudiantes en un archivo de registros o generar los datos de forma aleatoria, puede elegir
    una de las dos opciones pero no mezclarlas. Los datos deben agregarse al archivo de forma tal que se mantenga el
    conenido previo y se agreguen al final.
2 - Mostrar el contenido del archivo creado en el punto 1 (leer el nombre del archivo por teclado) pero filtrando solo
    los alunos del 7mo. año y mostrando al final una linea con la cantidad de alumnos del listado, si no hay registros
    con alumnos del 7mo. año informar con un mensaje.
3 - En base al archivo generado en el punto un cargar todos los registros del archivo en un vector de registros de forma
    el vector se mantenga ordenado por legajo en todo momento. La solución de cargar todo y ordenar al final no será
    tenida en cuenta.
    Mostrar el vector a razón de un registro por línea al finalizar la carga.
4 - Buscar en el vector si existe un alumno con legajo x_legajo (x_legajo se carga por teclado) y con deporte x_codigo
    (xcodigo también se carga por teclado), si existe mostrar sus datos y si no existe agregar un registro con los datos
    anteriores solicitando además se cargue por teclado el nombre y el año que cursa.
5 - Generar una matriz donde se cuente la cantidad de alumnos por deporte y año que cursa (10 * 7 = 70 contadores).
    Con la matríz geenrada mostrar todos los contadores de una actividad x que se carga por teclado.


"""


import validadores
import menus
import registro_inscripcion
from registro_inscripcion import Inscripcion

NOMBRE_ARCHIVO = 'salida.pydb'


def principal():
    vec_inscripciones = []
    opciones = ('1 - Crear registros en el archivo',
                '2 - Mostrar 7mo año del archivo',
                '3 -Generar vector y mostrar todos',
                '4 - Buscar por legajo',
                '5 - Generar matriz y mostrar por actividad',
                '6 - Salir')

    opc = None
    while opc != 6:
        menus.mostrar_menu('Gestión de Inscripciones', opciones)
        opc = validadores.leer_entero_valido('Ingrese su opción: ',
                                             limite_inferior=1,
                                             limite_superior=6)
        if opc == 6:
            print('Fin.')
        elif opc == 1:
            n = int(input('Cuantos datos desea generar y agregar?: '))
            vec_datos_nuevos = registro_inscripcion.generar_datos(n)
            registro_inscripcion.agregar_a_archivo(vec_datos_nuevos)
        elif opc == 2:
            nombre = input('Que archivo desea ver?: ')
            registro_inscripcion.mostrar_archivo(nombre)
        elif opc == 3:
            registro_inscripcion.generar_vector(vec_inscripciones)
            registro_inscripcion.mostrar_vector(vec_inscripciones)
        elif opc == 4:
            if len(vec_inscripciones) == 0:
                print('Primero debe generar el vector!')

            else:
                deportes = ('Basquet', 'Tenis', 'Rugby Seven', 'Handball', 'Voley', 'Ajedrez', 'Softball',
                            'Atletismo', 'Skate', 'Futbol')

                legajo = int(input('Que legajo desea buscar?: '))
                for i in range(len(deportes)):
                    print(f'{i}: {deportes[i]}')
                deporte = int(input('Que deporte practica?: '))
                persona = registro_inscripcion.buscar_por_legajo_y_deporte(vec_inscripciones, legajo, deporte)

                if persona:
                    print(registro_inscripcion.to_string(persona))

                else:
                    choice = int(input('Esa persona no existe. Desea agregarla? (Y=1/N=2):'))
                    if choice == 1:
                        nombre = input('Como se llama?: ')
                        anio = validadores.leer_entero_valido('Que año cursa?', 7)
                        nuevo = Inscripcion(legajo, nombre, anio, deporte)
                        registro_inscripcion.add_in_order_legajo(nuevo, vec_inscripciones)

                        print(f'{registro_inscripcion.to_string(nuevo)} \n'
                              f'se ha agregado correctamente')
                    else:
                        print('ok!')

        elif opc == 5:
            contadores = registro_inscripcion.generar_matriz()
            x = int(input('Que actividad desea ver?: '))
            registro_inscripcion.mostrar_matriz_de_act(contadores, x)
        input('\nPresione enter para continuar...\n')


if __name__ == '__main__':
    principal()
