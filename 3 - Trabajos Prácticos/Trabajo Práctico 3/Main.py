from modulo import *


def mostrar_menu_de_opciones():  # muestra el menu de opciones
    print('-' * 50)
    print('Bienvenido al Gestor de Libros de la biblioteca. \n')
    print('-' * 50)
    print(
        'A continuación, se le mostrarán las opciones posibles y usted podrá seleccionar una de ellas, escribiendo \n'
        'el número al que corresponde la opción deseada. \n\n'
        '1 -> Generar libros automáticamente. \n'
        '2 -> Agregar libros al sistema manualmente. \n'
        '3 -> Mostrar los datos de los libros en el sistema en orden alfabético. \n'
        '4 -> Mostrar la cantidad de libros por género, e indicar el género con más libros. \n'
        '5 -> Buscar el libro de mayor precio para un idioma. \n'
        '6 -> Buscar un libro por código ISBN. \n'
        '7 -> Mostrar los libros del género más popular, ordenados de mayor a menor precio. \n'
        '8 -> Consultar precio de un grupo de libros según su ISBN. \n'
        '9 -> Salir del programa\n')


def principal():
    # inicialización de variables necesarias
    genero_popular = 10
    op = 0
    libros = []

    # menu de opciones
    while op != 9:
        mostrar_menu_de_opciones()
        op = int(input('---- > Ingrese una opción: '))

        if op == 1:  # generar libros automáticamente
            n = int(input('Cuantos libros desea generar?: '))
            print('Generando libros...')
            generar_arreglo_aleatorio(n, libros)

            input('Presione enter para continuar...')
        if op == 2:  # cargar libros manualmente
            n = int(input('Cuantos libros desea agregar?: '))
            for i in range(n):
                libros.append(ingresar_datos_libro())

            input('Presione enter para continuar...')
        if op == 3:  # mostrar libros actualmente dentro del sistema

            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')

            else:
                mostrar_libros(libros)

                input('Presione enter para continuar...')

        if op == 4:  # mostrar libros por género y determinar el que más libros tiene

            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')
            else:
                genero_popular = contador_de_generos(libros)

                input('Presione enter para continuar...')

        if op == 5:  # mostrar el libro de mayor precio para un idioma en específico
            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')

            else:
                libro_precio_may, idi_selec = busqueda_de_mayor(libros)
                idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]
                idi_selec = idiomas[idi_selec - 1]
                print(f'El libro del idioma {idi_selec}, con mayor precio es "{libro_precio_may.titulo}"',
                      f' | ISBN {libro_precio_may.codigo}, con un precio de ${libro_precio_may.precio}')

                input('Presione enter para continuar...')

        if op == 6:  # buscar un libro por isbn
            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')

            else:
                buscado = input('Ingrese el código ISBN a buscar: ')
                resultado = buscar_por_isbn(libros, buscado)
                if resultado is False:
                    print('No se encontró el libro solicitado')
                else:
                    print(f'El libro buscado es: "{resultado.titulo}" y su precio es '
                          f'${round(resultado.precio * 1.10, 2)}')

                input('Presione enter para continuar...')

        if op == 7:  # mostrar los libros del género más popular ordenados por precio de mayor a menor
            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')

            else:
                consulta_de_un_genero(libros, genero_popular)

                input('Presione enter para continuar...')

        if op == 8:  # buscar múltiples libros según su ISBN

            if len(libros) == 0:  # validar que haya libros en el sistema
                print('No hay libros cargados en el sistema!!')
                input('Presione enter para continuar...')

            else:
                buscar_grupo_de_libros(libros)

                input('Presione enter para continuar...')

        if op <= 0 or op >= 10:  # validar que sea una opción correcta
            print('Por favor, ingrese un valor válido.')

            input('Presione enter para continuar...')

    print('Gracias por usar!')  # chau!


if __name__ == '__main__':
    principal()
