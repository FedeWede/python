"""
1) Determinar el promedio de vocales por palabra
2) Determinar la cantidad de palabras que tienen h, pero que no empiezan ni terminan con h.
3) Determinar la cantidad de palabras que contuvieron la silaba "en" dos veces.
4) Determinar la cantidad de palabras que terminan con "io" y tienen más de tres letras.
5) Determinar la cantidad de palabras que empiezan con la misma letra que terminó la palabra anterior.
"""


def test():
    # Inicializar variables
    c_letras = c_voc = t_voc = c_palabras = 0
    primer_letra = car_ant = car_ant_ant = letra_p_anterior = None
    punto_1 = punto_2 = punto_3 = punto_4 = punto_5 = 0
    h_word = en_word = p_word = False
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')

    # Ingresar el texto
    txt = receptor_de_texto()

    for car in txt:
        if car != ' ' and car != '.':
            c_letras += 1
            # chequear si es la primer letra
            if c_letras == 1:
                primer_letra = car
                if letra_p_anterior == car:
                    p_word = True

            # chequear si hay vocales
            if car in vocales:
                c_voc += 1

            if car == 'h':
                h_word = True

            # chequear cuantos "en" hay
            if car_ant == 'e' and car == 'n':
                en_word += 1

            # guardar última y anteúltima letra
            car_ant_ant = car_ant
            car_ant = car

        else:
            c_palabras += 1

            # saltear espacios
            if c_letras == 0:
                continue

            # promedio de vocales
            t_voc += c_voc
            punto_1 = t_voc / c_palabras

            # si la palabra tuvo h
            if h_word is True and primer_letra != 'h' and car_ant != 'h':
                punto_2 += 1

            # si la palabra tuvo "en" dos veces
            if en_word == 2:
                punto_3 += 1

            # si la palabra terminó con io
            if car_ant_ant == 'i' and car_ant == 'o' and c_letras > 3:
                punto_4 += 1

            # si empezó con la letra de la palabra anterior.
            if p_word:
                punto_5 += 1

            # resetear contadores
            c_letras = 0
            h_word = p_word = False
            letra_p_anterior = car_ant
            en_word = 0

    # resultados
    print(' > Promedio de vocales por palabra es: ', punto_1,
          '\n > La cantidad de palabras con H al medio es de:', punto_2,
          '\n > La cantidad de palabras que tuvieron la sílaba "en" dos veces es de: ', punto_3,
          '\n > La cantidad de palabras que terminan con "io" es de: ', punto_4,
          '\n > La cantidad de palabras que empezaron con la última letra de la palabra anterior es de :', punto_5)


def receptor_de_texto():
    cadena = input('> Ingrese un texto que termine con punto: ').lower()
    while cadena[-1] != '.':
        cadena = input('> El texto debe terminar con un punto, ingréselo de nuevo: ').lower()

    return cadena


if __name__ == '__main__':
    test()
