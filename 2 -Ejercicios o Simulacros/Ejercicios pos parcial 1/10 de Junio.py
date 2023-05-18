# Funciones
def vocal(letra):
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')
    if letra in vocales:
        check = 1
    else:
        check = 0
    return check


# Inicialización de vairables y banderas
def test():
    letter = letter_pw = words = vow = prev = lo_words = vow_p_word = three_vows = 0
    lo = False

    # Fin de inicialización

    # Introducción de cadena

    txt = input('Ingrese una reputísima cadena de caracteres: ').lower()

    # Verificar que termine con .

    while txt[-1] != '.':
        print('Tiene que tener un punto al final la oración, pelotudo.')
        txt = input('Escribilo de vuelta: ').lower()

    # Análisis de la cadena
    for char in txt:

        # Contador de letras por palabra y global

        if char != ' ' and char != '.':
            letter += 1
            letter_pw += 1

            # Contador de vocales
            vow += vocal(char)
            vow_p_word += 1

            # Contador de "lo"

            if prev == "l" and char == "o":
                lo = True
            prev = char

        else:

            # Ignorar el doble espacio

            if letter_pw == 0:
                continue

            # reseteador de contador de letras por palabra al finalizar una palabra
            # Contador de palabras

            else:
                words += 1
                letter_pw = 0

                # Verificar si una palabra tuvo 3 o más vocales
                if vow_p_word >= 3:
                    three_vows += 1
                    vow_p_word = 0

                # Verificar si la palabra anterior tuvo o no un "lo"

                if lo:
                    lo_words += 1
                    lo = False

    # Resultados
    print('El texto tiene\n', words, 'palabras', '\n', vow, 'vocales')
    print(' El promedio de letras por palabras es de', letter / words)
    print(' El promedio de vocales por palabras es de', vow / words)
    print(' El texto tiene', lo_words, 'palabras con "lo"')
    print(' Tuvo ', three_vows, 'palabras con 3 vocales')


if __name__ == '__main__':
    test()
