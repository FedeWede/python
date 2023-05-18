import random

descripciones = ('Arreglo', 'Expansion', 'Demolición', 'Pintado', 'Mantenimiento', 'Consulta',)
formas_de_pago = ('Efectivo', 'Crédito', 'Débito', 'Transferencia', 'Fiado')


class Servicio:
    def __init__(self, identificacion, descripcion, importe, tipo, medio_pago):
        self.id = identificacion
        self.descripcion = descripcion
        self.importe = importe
        self.tipo = tipo
        self.medio_pago = medio_pago

    def __str__(self):
        return (f'ID: {self.id} | '
                f'Descripcion: {self.descripcion} |'
                f'Importe: {self.importe} | '
                f'Tipo de servicio: {self.tipo} | '
                f'Medio de pago: {formas_de_pago[self.medio_pago]}')


def generar_registo():
    identificacion = random.randint(1000, 5000)
    descripcion = random.choice(descripciones)
    importe = round(random.random() * 5000 + 500, 2)
    tipo = random.randint(0, 24)
    medio_pago = random.randint(0, 4)

    reg = Servicio(identificacion, descripcion, importe, tipo, medio_pago)

    return reg
