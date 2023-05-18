def validar_entre(inferior, superior, mensaje_ingreso='Ingrese un valor:', mensaje_error='Valor inválido. Reintente'):
    val = int(input(mensaje_ingreso))
    while val < inferior or val > superior:
        print(mensaje_error)
        val = int(input(mensaje_ingreso))
    return val


def validar_mayor_igual(inferior, mensaje_ingreso='Ingrese un valor:', mensaje_error='Valor inválido. Reintente'):
    val = int(input(mensaje_ingreso))
    while val < inferior:
        print(mensaje_error)
        val = int(input(mensaje_ingreso))
    return val


def validar_nombres():
    name = input('Ingrese un nombre con 8 caracteres y que termine con .txt: ')
    while len(name) != 12 or not (name.endswith('.txt')):
        name = input('El nombre debe tener 8 caracteres y terminar con .txt: ')

    return name


def validar_caracteres(cadena):
    res = True
    for car in cadena:
        if not (car in 'epfd'):
            res = False
            break
    return res


def validar_contenido():
    cont = input('Ingrese el contenido del archivo: ')
    while (len(cont) < 1 or len(cont) > 4) or not validar_caracteres(cont):
        cont = input('No puede ser vacío, ni tener letras repetidas: ')

    return cont
