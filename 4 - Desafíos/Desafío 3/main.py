from soporte import *


def parte_1():
    vec = vector_unknown_range(300000)

    num = []
    cont = []

    for i in range(len(vec)):
        index = search(num, vec[i])

        if index != -1:
            cont[index] += 1

        else:
            num.append(vec[i])
            cont.append(1)

    print('Respuesta 1: ', len(num))

    mayor, indice = buscar_mayor(num)  # parte 2
    print('Respuesta 2: ', mayor)
    print('Respuesta 3: ', cont[indice])


def parte_2():
    vec = vector_known_range(300000)
    c = [0] * 300000
    contador = 0
    for i in vec:
        c[i] += 1
    for i in range(len(c)):
        if c[i] != 0:
            contador += 1

    print(f'Respuesta 5: {contador}')

    veces_moda, numero_modal = buscar_mayor(c)
    print(f'Respuesta 6: {numero_modal}')
    print(f'Respuesta 7: {veces_moda}')


if __name__ == '__main__':
    parte_1()
    parte_2()