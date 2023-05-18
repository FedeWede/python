"""
Hay que cargar una cadena de caracteres, de ahi ver cuantas palabras tuvo la cadena, cuants palabras empiezan  con "P"
y cuantas  palabras tienen los caracteres "Ta"
"""

palabras = 0
cantp = 0
primer_letra = True
letra_anterior = None
ta = 0
palabra_ta = False

texto = input('Type a text: ')

for letra in texto:
    if primer_letra:
        primer_letra = False
        if letra == 'p' or letra == 'P':
            cantp += 1
    if letra == " " or letra == '.':
        palabras += 1
        if palabra_ta is True:
            ta += 1
            palabra_ta = False
    else:
        if letra_anterior == " " and letra == 'p' or letra == 'P':
            cantp += 1
        if (letra_anterior == 'T' or letra_anterior == 't') and (letra == 'A' or letra == 'a'):
            palabra_ta = True

    letra_anterior = letra
print('La cantidad de palabras es de:', palabras,
      '\n La  cantidad de palabras que empiezan con p es de: ', cantp,
      '\n La cantidad de palabras que tienen "ta" es de: ', ta)
