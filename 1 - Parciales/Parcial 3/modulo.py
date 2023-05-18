import random


class Alquiler:
    def __init__(self, id_alquiler, descripcion, tipo, importe, cant_dias):
        self.id_alquiler = id_alquiler
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.cant_dias = cant_dias

    def __str__(self):
        return f'ID del alquiler: {self.id_alquiler} | ' \
               f'Descripcion del coche: {self.descripcion} | ' \
               f'Tipo de vehículo: {self.tipo} | ' \
               f'Importe del alquiler: {self.importe} | ' \
               f'Cantidad de días alquilado: {self.cant_dias}'


def validar_id(id_alquiler):
    if id_alquiler < 0:
        return False
    else:
        return True


def colores():
    color = ('Rojo', 'Blanco', 'Gris', 'Negro', 'Azul', 'Verde', 'Amarillo')

    return color


def carga_automatica(n, vec):
    for i in range(n):
        id_alquiler = random.randint(100, 999)
        descripcion = random.choice(colores())
        tipo = random.randint(1, 10)
        importe = random.randint(1000, 3000)
        cant_dias = random.randint(1, 30)

        auto = Alquiler(id_alquiler, descripcion, tipo, importe, cant_dias)
        vec.append(auto)

    print('Alquileres generados!')


def carga_manual(n, vec):
    for i in range(n):
        id_alquiler = int(input('Ingrese un id de alquiler: '))
        validacion = validate(id_alquiler)
        while not validacion:
            id_alquiler = int(input('Ingrese un id válido: '))
            validacion = validate(id_alquiler)

        descripcion = input('Descripcion del coche: ')

        tipo = int(input('Tipo de coche: '))
        validacion_tipo = validar_tipo(tipo)
        while not validacion_tipo:
            tipo = int(input('Ingrese un tipo de coche válido: '))
            validacion_tipo = validate(tipo)

        importe = int(input('Ingrese el importe del alquiler: '))
        validacion_importe = validate(importe)
        while not validacion_importe:
            importe = int(input('Ingrese el importe del alquiler válido: '))
            validacion_importe = validate(importe)

        cant_dias = int(input('Ingrese la cantidad de días para alquilar: '))
        validacion_dias = validate(cant_dias)
        while not validacion_dias:
            cant_dias = int(input('Ingrese la cantidad de días para alquilar: '))
            validacion_dias = validate(cant_dias)

        alquiler = Alquiler(id_alquiler, descripcion, tipo, importe, cant_dias)
        vec.append(alquiler)

    print('Se han cargado todos los alquileres!')


def validate(x):
    if x <= 0:
        return False
    else:
        return True


def validar_tipo(tipo):
    if tipo <= 0 or tipo > 10:
        return False
    else:
        return True


def bubble_sort_importe(vec):
    n = len(vec)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec[j].importe > vec[j + 1].importe:
                ordenado = False
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if ordenado:
            break


def mostrar_vector(vec):
    for i in range(len(vec)):
        print(vec[i])


def contar_alquileres_por_tipo(vec):
    contadores = [0] * 10

    for i in range(len(vec)):
        contadores[vec[i].tipo - 1] += 1

    return contadores


def mostrar_contadores(vec):
    for i in range(len(vec)):
        if vec[i] != 0:
            print(f'La cantidad de autos tipo {i + 1} es {vec[i]}')


def buscar_mayor_importe(vec):
    mayor_importe = 0
    res = None
    for i in range(len(vec)):
        if vec[i].importe > mayor_importe:
            mayor_importe = vec[i].importe
            res = vec[i]

    return res


def calcular_promedio(vec):
    suma = 0
    for i in range(len(vec)):
        suma += vec[i].importe

    return suma / len(vec)


def buscar_por_descripcion(vec, descripcion):
    for i in range(len(vec)):
        if descripcion == vec[i].descripcion:
            return vec[i]

    return False


def buscar_por_importe_y_descripcion(vec, importe, descripcion):
    for i in range(len(vec)):
        if importe <= vec[i].importe and descripcion == vec[i].descripcion:
            return vec[i]

    return False


def buscar_alquiler(vec, desc, importe):
    desc = buscar_por_descripcion(vec, desc)
    if desc is False:
        print('No se ha encontrado un auto con esa descripción.')
        return -1

    importe = buscar_por_importe_y_descripcion(vec, importe, desc.descripcion)

    if importe is False:
        print('No se ha encontrado un alquiler para ese importe')
        return -1

    return importe
