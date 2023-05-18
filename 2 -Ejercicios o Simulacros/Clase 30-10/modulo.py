import random
import os
import pickle

nombres = ('Carlos', 'Pepe', 'Fede', 'Charlie', 'Felipe', 'Eduardo', 'Valentina', 'Guillermo', 'Tuvieja',)
tipos = ('Velero', 'Orza', 'Lancha', 'Moto de agua', 'Remo')



class Embarcacion:
    def __init__(self, matricula, propietario, parcela, tipo, monto):
        self.matricula = matricula
        self.propietario = propietario
        self.parcela = parcela
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        global tipos
        return f'Matricula: {self.matricula} | ' \
               f'Propietario: {self.propietario} | ' \
               f'Parcela: {self.parcela} | ' \
               f'Tipo: {tipos[self.tipo]} | ' \
               f'Monto: {self.monto}'


def crear_matricula():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras = ''
    for i in range(3):
        letras += random.choice(alfabeto)
    numeros = random.randint(1000, 9999)
    matricula = letras + str(numeros)

    return matricula


def add_in_order(reg, vec):
    n = len(vec)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].matricula == reg.matricula:
            pos = c
            break
        if reg.matricula < vec[c].matricula:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def crear_reg():
    global nombres
    matricula = crear_matricula()
    propietario = random.choice(nombres)
    parcela = random.randint(0, 24)
    tipo = random.randint(0, 4)
    monto = random.randint(1000, 5000)

    barco = Embarcacion(matricula, propietario, parcela, tipo, monto)

    return barco


def crear_vector():
    vec = []
    cant = int(input('Cuantas embarcaciones desea crear?: '))

    for i in range(cant):
        barco = crear_reg()
        add_in_order(barco, vec)

    return vec


def crear_archivo(vec, nombre):
    if os.path.exists(nombre):
        print('Ese archivo ya existe!')
        return
    print('0: Velero | 1: Orza | 2: Lancha | 3: Moto de agua | 4: Remo')
    tipo = int(input('Que tipo de embarcaciones desea cargar en el archivo?: '))
    contador = 0

    arch = open(nombre, 'wb')
    for i in range(len(vec)):
        if tipo == vec[i].tipo:
            contador += 1
            pickle.dump(vec[i], arch)
    print(f'Archivo creado con {contador} registros')

    arch.close()


def leer_archivo(nombre):
    if not os.path.exists(nombre):
        print('flaco!')
        return

    arch = open(nombre, 'rb')
    tam = os.path.getsize(nombre)
    print('Contenido: ')
    while arch.tell() < tam:
        reg = pickle.load(arch)
        print(reg)

    arch.close()


def crear_matriz(vec):
    mat = [[0] * 5 for i in range(25)]
    # mat[0,25][0,5]

    for i in range(len(vec)):
        fil = vec[i].parcela
        col = vec[i].tipo
        mat[fil][col] += vec[i].monto

    return mat


def mostrar_matriz(mat):
    global tipos
    print(len(mat))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print(f'Parcela: {i} Tipo: {tipos[j]}: Total: {mat[i][j]}')


def buscar_por_matricula(vec, matricula):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].matricula == matricula:
            pos = c
            break
        if matricula < vec[c].matricula:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    return pos


def buscar_por_nombre(vec, nombre):
    for i in range(len(vec)):
        if nombre == vec[i].propietario:
            return vec[i]

    return False


def generar_vector_parcelas(vec, parcela):
    vec_parcelas = []
    for i in range(len(vec)):
        if parcela == vec[i].parcela:
            vec_parcelas.append(vec[i])

    ordenar_por_nombre(vec_parcelas)

    return vec_parcelas


def ordenar_por_nombre(vec):
    n = len(vec)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec[j].propietario > vec[j + 1].propietario:
                ordenado = False
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if ordenado:
            break

