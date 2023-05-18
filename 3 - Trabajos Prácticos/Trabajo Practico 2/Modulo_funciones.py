from random import randint


# para tirar los 3 dados

def dados():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    return d1, d2, d3


# retorna true si n1 es par

def check_paridad(n1):
    return n1 % 2 == 0


# un turno de un jugador. devuelve un 1 si acertó la paridad, y el puntaje de esa ronda

def juego(nombre):
    print(nombre, ', ¿Apuesta por impar o por par?"')
    eleccion = int(input('> Ingrese 1 para impar o 2 para par: '))

    # verificador
    while 2 < eleccion > 1:
        eleccion = int(input('> Por favor ingrese un valor entre 1 y 2: '))

        # eleccion impar
    if eleccion == 1:
        input('Eligio impar, presione ENTER para tirar los dados...')

        # tirar dados
        dado1, dado2, dado3, = dados()
        paridad = check_paridad(dado1 + dado2 + dado3)
        # mostrar resultados
        print("\n*Su primer dado fue: ", dado1, "*\n*Su segundo dado fue: ", dado2, "*\n*Su tercer dado fue: ", dado3,
              "*""\n*Sus dados suman un total de: ", dado1 + dado2 + dado3)
        if not paridad:
            puntaje = (max(dado1, dado2, dado3))
            acierto = 1
            print('> Al acertarle a la paridad, suma ', puntaje, 'puntos')
            print(10 * '*')
            if not check_paridad(dado1) and not check_paridad(dado2) and not check_paridad(dado3):
                puntaje *= 2
                print('> Al ser todos los dados impares, se duplica su puntaje')
                print(10 * '*')
        else:
            puntaje = -(min(dado1, dado2, dado3))
            acierto = 0
            print('> Al no acertarle a la paridad, resta', min(dado1, dado2, dado3), ' puntos')
            print(10 * '*')

    # si elije par
    else:
        input('Eligio par, presione ENTER para tirar los dados...')

        # tirar dados
        dado1, dado2, dado3, = dados()
        paridad = check_paridad(dado1 + dado2 + dado3)

        # mostrar resultados
        print("\n*Su primer dado fue: ", dado1, "*\n*Su segundo dado fue: ", dado2, "*\n*Su tercer dado fue: ", dado3,
              "*""\n*Sus dados suman un total de: ", dado1 + dado2 + dado3)
        if paridad:
            puntaje = (max(dado1, dado2, dado3))
            acierto = 1
            print('> Al acertarle a la paridad, suma ', puntaje, 'puntos')
            print(10 * '*')
            if check_paridad(dado1) and check_paridad(dado2) and check_paridad(dado3):
                puntaje *= 2
                print('> Al ser todos los dados pares, se duplica su puntaje')
                print(10 * '*')
        else:
            puntaje = -(min(dado1, dado2, dado3))
            acierto = 0
            print('> Al no acertarle a la paridad, resta', min(dado1, dado2, dado3), ' puntos')
            print(10 * '*')
    return acierto, puntaje
