"""
1) Cantidad de palabras que tuvieron al menos un dígito y también la letra "r"
2) Determinar el porcentaje de palabras que comenzaron con vocal y terminaron en consonante
3) Determinar cuantas palabras comenzaron con la misma letra que terminó la palabra anterior
4) Determinar el promedio de letras por palabras, pero solo de las palabras que tuvieron
al menos una "a" en la primera mitad y terminaron en "er"
"""


def ingreso():
    texto = input('> Ingrese un texto que termine con punto: ')
    while texto[-1] != '.':
        texto = input('> El texto debe terminar con un punto: ')

    return texto


def test():
    # Inicializar variables
    c_letras = c_palabras = posicion_a = t_letras = t_palabras = 0
    punto_1 = punto_2 = punto_3 = punto_4 = 0
    car_ant = primera_letra = ultima_letra = car_ant_ant = None
    hay_digito = hay_r = hay_a = False
    digitos = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')

    # Ingresar texto
    txt = ingreso()

    for car in txt:
        if car != ' ' and car != '.':
            c_letras += 1
            # registrar primer letra
            if c_letras == 1:
                primera_letra = car

            # punto 2
            if car in digitos:
                hay_digito = True
            if car == 'r':
                hay_r = True

            car_ant_ant = car_ant
            car_ant = car

            # punto 3
            if car == 'a' and hay_a is False:
                hay_a = True
                posicion_a = c_letras

        else:
            # chequear si hubo palabra
            if c_letras == 0:
                continue
            # contar palabras
            c_palabras += 1

            # primer punto
            if hay_r and hay_digito:
                punto_1 += 1

            # segundo punto
            if primera_letra in vocales and car_ant not in vocales:
                punto_2 += 1

            # tercer punto
            if primera_letra == ultima_letra:
                punto_3 += 1
            ultima_letra = car_ant

            # cuarto punto
            if hay_a is True and car_ant == 'r' and car_ant_ant == 'e' and (posicion_a <= c_letras / 2):
                t_palabras += 1
                t_letras += c_letras
                punto_4 = t_letras // t_palabras

            # resetear variables
            hay_r = hay_digito = False
            c_letras = 0

    print('La cantidad de palabras con un dígito y la letra R: ', punto_1)
    print('Porcentaje de palabras que empezaron en vocal y terminaron en consonante: ', punto_2 * 100 // c_palabras)
    print('Cantidad de palabras que empezaron con la misma letra que terminó la letra anterior: ', punto_3)
    print('Promedio de letras por palabras que tuvieron una "a" y terminaron con "er"', punto_4)


if __name__ == '__main__':
    test()
