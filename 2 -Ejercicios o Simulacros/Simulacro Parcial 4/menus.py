__author__ = 'philip'


def mostrar_menu(titulo, opciones):
    print('*' * (len(titulo) + 4))
    print('*',titulo,'*')
    print('*' * (len(titulo) + 4))
    print()
    for opcion in opciones:
        print(opcion)


def prueba():
    opcs = '1 - Suma',\
            '2 - Producto', \
            '3 - Factorial', \
            '4 - Salir'
    mostrar_menu('Menú de Opciones', opcs)


if __name__ == '__main__':
    prueba()