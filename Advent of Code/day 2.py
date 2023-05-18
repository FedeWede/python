def define_number(string):  # recorre caracter por caracter y frena cuando detecta el -, guarda el primer número y
    # despues sigue hasta el espacio, guardando el segundo numero
    first = True
    minimum = ''
    maximum = ''
    for char in string:
        if char != '-' and char != ' ':
            if first:
                minimum += char
            else:
                maximum += char
        else:
            first = False
            if char == '-':
                continue
            elif char == ' ':
                break

    return minimum, maximum


def define_letter(string):  # recorre caracter por caracter cada fila, se saltea la primera parte y guarda la primer
    # letra
    for char in string:
        if char in '1234567890' or char in '-' or char in ' ':
            continue
        else:
            letter = char
            return letter


""" 
def validate(minimum, maximum, letter, string):   # este usé para la primera parte
    spaces = counter = 0.
    start = False
    for char in string:
        if start is True and char == letter:
            counter += 1
        if char == ' ':
            spaces += 1
            if spaces == 2:
                start = True

    if counter < minimum or counter > maximum:
        return 0
    else:
        return 1
"""


def validate(minimum, maximum, letter, string):  # este usé para la segunda parte
    spaces = count = 0.
    start = pos_1 = pos_2 = False
    for char in string:
        if start is True:
            count += 1
            if count == minimum and char == letter:
                pos_1 = True
            elif count == maximum and char == letter:
                pos_2 = True

        if char == ' ':
            spaces += 1
            if spaces == 2:
                start = True

    if (pos_1 is True and pos_2 is False) or (pos_1 is False and pos_2 is True):
        return 1
    else:
        return 0


def test():  # función principal
    counter = 0
    with open("input_2.txt") as _file:
        codes = []
        for line in _file:
            codes.append(line)
    for i in range(len(codes)):
        minimum, maximum = define_number(codes[i])
        letter = define_letter(codes[i])
        counter += validate(int(minimum), int(maximum), letter, codes[i])
    print(f'la cantidad de contraseñas validas es de: {counter}')


if __name__ == "__main__":
    test()
