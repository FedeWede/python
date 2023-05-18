"""
1) Determinar la cantidad promedio de vocales (minúsculas o mayúsculas) entre todas las palabras del texto.
Por ejemplo, en el texto “No hay gloria sin esfuerzo.”, hay un total de 5 palabras, y un total de 10 vocales.
Por lo tanto, el promedio pedido es 2 vocales por palabra.

2) Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que finalizan con el primer
caracter de todo el texto (minúscula o mayúscula si es letra).
Por ejemplo, en el texto: "Antes de ahora no sabia nada.", hay 3 palabras que cumplen con la condición
("antes", "ahora" y "nada") sobre un total de 6 palabras. Por lo tanto, el porcentaje pedido es del 50%.

3) Determinar la cantidad de palabras que incluyeron una "r" (minúscula o mayúscula) entre las primeras dos posiciones,
pero no contuvieron una "n" entre las posiciones tres y cuatro.
Por ejemplo, en el texto: "Rara vez renueva el armario.”, hay 2 palabras que cumplen: "Rara" y "armario".
La palabra "renueva" no cuenta, porque si bien tiene una "r" entre las primeras dos, tiene también una "n" en la
posición tres.

4) Determinar la cantidad de palabras que contienen la expresión "br" (con cualquiera de sus letras en minúscula o en
mayúscula) pero de forma que la palabra no comience con la letra "a" (mayúscula o minúscula).
Por ejemplo, en el texto: "Nos abrazamos porque en abril volvemos a Brasil.", hay 1 palabra que cumple con la condición
("Brasil"). Las palabras "abrazamos" y "abril" tienen "br", pero no cuentan porque comienzan con "a".

"""

__author__ = 'Wedemeyer Federico, 90328'


# función ingresar y verificar texto
def ingreso():
    texto = input('> Ingrese un texto que termine con punto: ').lower()
    while texto[-1] != '.':
        texto = input('> El texto debe terminar con un punto: ').lower()

    return texto


# calcular porcentaje
def porcentaje(valor1, valor2):
    res = valor1 * 100 // valor2

    return res


def test():
    # inicializar variables
    punto_1 = punto_2 = punto_3 = punto_4 = 0
    c_letras = c_palabras = c_vocales = car_ant = palabras_punto_2 = pos_r = pos_n = 0
    primera_letra_texto = primera_letra_palabra = None
    hay_r = hay_n = hay_br = False
    primera_palabra = True
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')
    # ingresar texto
    txt = ingreso()

    # recorrer texto
    for car in txt:
        # dividir análisis entre letras y palabras completas
        if car != ' ' and car != '.':
            c_letras += 1
            # punto 1
            if car in vocales:
                c_vocales += 1
            # punto 2
            if primera_palabra:
                primera_letra_texto = car
                primera_palabra = False
            # punto 3
            if car == 'r':
                if not hay_r:
                    pos_r = c_letras
                    hay_r = True
            if car == 'n':
                if not hay_n:
                    hay_n = True
                    pos_n = c_letras
            # punto 4
            if car_ant == 'b' and car == 'r':
                hay_br = True
            if c_letras == 1:
                primera_letra_palabra = car

            # guardar letra anterior
            car_ant = car

        else:

            # chequear si hubo palabra
            if c_letras == 0:
                continue

            # contar palabras
            c_palabras += 1

            # punto 1
            punto_1 = c_vocales / c_palabras
            # punto 2
            if car_ant == primera_letra_texto:
                palabras_punto_2 += 1
            punto_2 = porcentaje(palabras_punto_2, c_palabras)
            # punto 3
            if hay_r and pos_r <= 2:
                punto_3 += 1
                if hay_n and (pos_n == 3 or pos_n == 4):
                    punto_3 -= 1
            # punto 4
            if hay_br and primera_letra_palabra != 'a':
                punto_4 += 1
            # resetear variables
            c_letras = pos_r = 0
            hay_r = hay_n = hay_br = False

    # resultados
    print('-' * 5, 'Respuestas', '-' * 5)
    print('> El promedio de vocales por palabras es de: ', round(punto_1, 2))
    print('> El porcentaje de palabras que finalizan con el primer carácter de todo el texto es de: ', punto_2, '%')
    print('> Las cantidad de palabras que tuvieron una "r" en sus dos primeros lugares y ninguna "n" en su tercera o '
          'cuarta posición es de: ', punto_3)
    print('> La cantidad de palabras que tuvieron un "br" pero su primera letra no era la "a" es de: ', punto_4)


if __name__ == '__main__':
    test()
print("\nFeliz cumple fede :D by Diegacho")

# hola profe :D
