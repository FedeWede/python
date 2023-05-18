import os
import random
import pickle

NOMBRES = ['Nico', 'Andy', 'Lucas', 'Juan', 'Jere', 'Rafa', 'Pablo', 'Lautaro', 'Rodrigo', 'Romi', 'Sole', 'Euge', 'Lauri', 'Tati', 'Sabri', 'Cande', 'Cami']
APELLIDOS = ['Steffo', 'Martinez', 'Peralta', 'Morinigo', 'Gasquez', 'Zavalía', 'Giannetto', 'Conforti', 'Brito', 'Lopez']
DESCRIPCION_TIPO = ['Basquet', 'Tenis', 'Rugby Seven', 'Handball', 'Voley', 'Ajedrez', 'Softball', 'Atletismo', 'Skate', 'Futbol']


class Inscripcion:
    def __init__(self, leg, nom, anio, cod):
        self.legajo = leg
        self.nombre = nom
        self.anio = anio
        self.codigo = cod


def to_string(reg):
    return 'Inscripción: ' + str(reg.legajo) + \
        ' | Nombre: ' + reg.nombre + \
        ' | Año: ' + str(reg.anio) + \
        ' | Actividad: [' + str(reg.codigo) + '] ' + DESCRIPCION_TIPO[reg.codigo]


def crear_aleatorio():
    leg = random.randint(1000, 9999)
    nom = random.choice(NOMBRES) + ' ' + random.choice(APELLIDOS)
    anio = random.randint(1,7)
    cod = random.randint(0,9)
    return Inscripcion(leg, nom, anio, cod)


def generar_datos(n):
    datos = []
    for i in range(n):
        reg = crear_aleatorio()
        datos.append(reg)

    return datos


def agregar_a_archivo(vec):
    if os.path.exists('salida.pydb'):
        contador = 0
        arch = open('salida.pydb', 'ab')
        for i in range(len(vec)):
            pickle.dump(vec[i], arch)
            contador += 1
        arch.close()
        print(f'Se han agregado {contador} registros al archivo "salida.pydb"')
    else:
        contador = 0
        arch = open('salida.pydb', 'wb')
        for i in range(len(vec)):
            pickle.dump(vec[i], arch)
            contador += 1
        arch.close()
        print(f'Se han agregado {contador} registros al archivo "salida.pydb"')


def mostrar_archivo(nombre):
    if not os.path.exists(nombre):
        print('No existe ese archivo.')
        return
    else:
        contador_alumnos = 0
        arch = open(nombre, 'rb')
        tam = os.path.getsize(nombre)
        while arch.tell() < tam:
            reg = pickle.load(arch)
            if reg.anio == 7:
                print(to_string(reg))
                contador_alumnos += 1
        print(f'La cantidad de alumnos de 7mo es de: {contador_alumnos}')


def add_in_order_legajo(reg, vec):
    n = len(vec)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].legajo == reg.legajo:
            pos = c
            break
        if reg.legajo < vec[c].legajo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def generar_vector(vec):
    arch = open('salida.pydb', 'rb')
    tam = os.path.getsize('salida.pydb')
    while arch.tell() < tam:
        reg = pickle.load(arch)
        add_in_order_legajo(reg, vec)
    arch.close()


def mostrar_vector(vec):
    for i in range(len(vec)):
        print(to_string(vec[i]))


def buscar_por_legajo_y_deporte(vec, legajo, deporte):
    for i in range(len(vec)):
        if legajo == vec[i].legajo and deporte == vec[i].codigo:
            return vec[i]

    return False


def generar_matriz():
    mat = [[0] * 7 for i in range(10)]
    # mat[0,25][0,5]

    arch = open('salida.pydb', 'rb')
    tam = os.path.getsize('salida.pydb')
    while arch.tell() < tam:
        reg = pickle.load(arch)
        fil = reg.codigo
        col = reg.anio - 1
        mat[fil][col] += 1
    arch.close()

    return mat


def mostrar_matriz_de_act(vec, x):
    print(len(vec))
    for c in range(len(vec[x])):
        print('En el anio ', c + 1, 'hay ', vec[x][c], 'alumnos')