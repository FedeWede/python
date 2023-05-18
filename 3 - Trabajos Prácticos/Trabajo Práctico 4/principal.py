from modulo import *


def Principal():
    op = 0
    libros = []
    matriz = 0
    while op != 8:
        menu_de_opciones()
        op = validar_entre('Ingrese una opción: ', 8, 1)

        if op == 1:
            libros = procesar_archivo()
            ver = validar_entre('Desea verlos? 1: Si/ 2: No:\n-> ', 2, 1)
            if ver == 1:
                mostrar_vector(libros)
                print('\nEsos son todos los libros disponibles.')
                input('Presione enter para continuar...')
            else:
                print('ok!')

        elif op == 2:
            if len(libros) == 0:
                print('No se ha cargado el archivo. Seleccione la opción 1.')
                input('Presione enter para volver al menú')
            else:
                sumar_revision(libros)
                input('Presione enter para continuar...')

        elif op == 3:
            if len(libros) == 0:
                print('No se ha cargado el archivo. Seleccione la opción 1.')
                input('Presione enter para volver al menú')
            else:
                mayor = buscar_mayor_revisiones(libros)
                promedio = calcular_promedio_idioma(libros, mayor.idioma)
                ejercicio_3(mayor, promedio)
                input('Presione enter para continuar...')

        elif op == 4:
            if len(libros) == 0:
                print('No se ha cargado el archivo. Seleccione la opción 1.')
                input('Presione enter para volver al menú')
            else:
                matriz = llenar_matriz(libros)
                input('Presione enter para continuar...')
                # mostrar_matriz(matriz)
                # no sabíamos si era necesario mostrar la matriz, así que por las dudas dejamos comentada la función

        elif op == 5:
            mostrar_decadas(libros)
            input('Presione enter para continuar...')

        elif op == 6:
            if matriz == 0:
                print('Primero debe generar la matriz.')
                input('Presione enter para volver al menu')
            else:
                generar_archivo(matriz)
                input('Presione enter para continuar')

        elif op == 7:
            leer_archivo()
            input('Presione enter para continuar')

    print('Chau!')


if __name__ == '__main__':
    Principal()
