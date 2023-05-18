"""
1) Cantidad de palabras que comienzan con la última letra de la primera palabra del texto.
2) El orden de la palabra más corta del texto.
3) Cantidad de palabras que tuvieron la sigla "mi" en la primera mitad de la palabra.
4) Cantidad de palabras que empiezan con "lo" y además tuvieron una "l" en la segunda mitad.
"""


def test():
    # Inicializar variables
    letra_p_p = punto_1 = punto_2 = primera_letra = cont_pal = punto_3 = pos_l = punto_4 = 0
    mi_word = lo_word = False
    ult_letra = car_ant = 1
    min_pal = pos_mi = None

    # Ingresar el texto
    txt = input('> Ingrese una cadena de caracteres: ').lower()
    while txt[-1] != '.':
        txt = input('> Tiene que tener un punto al final: ').lower()

    for car in txt:

        # Tratamiento por letras
        if car != ' ' and car != '.':

            # Contador de letras
            letra_p_p += 1

            # Guardar primer letra de la palabra
            if letra_p_p == 1:
                primera_letra = car
                car_ant = car

            # Chequear si hay un "mi" y guardar su posición
            if car_ant == 'm' and car == 'i':
                mi_word = True
                pos_mi = letra_p_p

            # Función lo
            lo_word, pos_l = lo_check(primera_letra, car_ant, car, letra_p_p)

            # Guardar la letra anterior
            car_ant = car

        # Tratamiento por palabras
        else:
            # No se contó una palabra, continuar.
            if letra_p_p == 0:
                continue

            # Contar las palabras y tratamiento para esa primer palabra
            cont_pal += 1
            if cont_pal == 1:
                ult_letra = car_ant
                min_pal = letra_p_p
                punto_2 = 1

            # Contador del punto 1
            if primera_letra == ult_letra:
                punto_1 += 1

            # Contador del punto 2
            if min_pal > letra_p_p:
                min_pal = letra_p_p
                punto_2 = cont_pal

            # Contador del punto 3
            if mi_word is True and pos_mi <= letra_p_p / 2:
                punto_3 += 1

            # Contador del punto 4
            if lo_word is True and pos_l >= letra_p_p / 2:
                punto_4 += 1

            # Resetear variables
            car_ant = 0
            letra_p_p = 0
            mi_word = False
            lo_word = False

    # Muestra de resultados
    print('Cantidad de palabras que comienzan con la última letra de la primer palabra: ', punto_1)
    print('El orden de la palabras mas chica: ', punto_2)
    print('Palabras con la sigla "mi" en la primera mitad', punto_3)
    print('Palabras que empiezan con lo y una l en la segunda mitad: ', punto_4)


def lo_check(primera, anterior, actual, cant_letras):
    condicion = False
    pos = 0
    # Chequear si empieza con "lo"
    if primera == 'l' and anterior == 'l' and actual == 'o':
        condicion = True
    # Chequear si la palabra con "lo" tiene una "l" y guardar su posición
    if condicion is True and actual == 'l':
        pos = cant_letras

    return condicion, pos


# Incializador del programa
if __name__ == '__main__':
    test()
