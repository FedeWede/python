__author__ = 'philip'


def leer_entero_valido(msg, limite_superior, limite_inferior = 0):
    x = int(input(msg))
    while x < limite_inferior or x > limite_superior:

        print('El valor deber estar entre', limite_inferior,
                'y', limite_superior, ' no sea perejil....')
        x = int(input(msg))
    return x


def leer_entero_positivo(msg):

    x = int(input(msg))
    while x <= 0:

        print('El valor deber ser positivo no sea perejil....')
        x = int(input(msg))
    return x


def prueba():
    print('Modulo validadores valor de __name__', __name__)
    print('Leer entero entr 1 y 10')
    n = leer_entero_valido('Ingrese la nota: ', 1, 10)
    print('La nota ingresada es:', n)


if __name__ == '__main__':
    prueba()
