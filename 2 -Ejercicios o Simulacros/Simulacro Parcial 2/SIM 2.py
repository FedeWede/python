from Funcion import conversor

# Menu de opciones
op = 0

while op != 3:
    print('Elija una opcion (1- Ciclistas / 2- Texto / 3- Salir)')
    op = int(input('Elegir: '))
    if op == 1:
        Guille = False
        fastest = winner = 0
        first = True
        for i in range(3):
            athl = input('Ingrese el nombre del atleta ' + str(i + 1) + ': ')
            time = int(input('Ingrese su tiempo: '))
            while time < 0:
                print('Tiene que ser un valor positivo papo')
                time = int(input('Ingrese su tiempo: '))
            if first is True:
                winner = athl
                fastest = time
                first = False
            elif time < fastest:
                winner = athl
                fastest = time
            if athl == 'Guille':
                Guille = True
        h, m, s = conversor(fastest)
        print('El ganador es ', winner, 'su tiempo fue de', h, 'hs', m, 'm', s, 's')
        if Guille is True:
            print('Terrible pete el Guille ese')
        if fastest < 850:
            print('Ha roto el record mundial!')

# OPCION 2
    elif op == 2:
        ps = 0
        js = 0
        total = 0
        text = input('Ingrese un texto: ').lower()
        for char in text:
            total += 1
            if char == 'p':
                ps += 1
            elif char == 'j':
                js += 1
        print('Hay ', ps, 'letras P en el texto, representando un total del ', (ps/total*100), '% del texto')
        print('Hay ', js, 'leteras J en el texto, representando un total del ', (js/total*100), '% del texto')

# SI LE ERRAS
    else:
        print('Entre el 1 y el 3, perejil')
