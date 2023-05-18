from modulo import *
import random


class Alumno:
    def __init__(self, dni_alumno, nombre, apellido, dni_tutor, cuota, nivel):
        self.dni_alumno = dni_alumno
        self.nombre = nombre
        self.apellido = apellido
        self.dni_tutor = dni_tutor
        self.cuota = cuota
        self.nivel = nivel

    def __str__(self):
        return f'Dni Alumno: {self.dni_alumno} | ' \
               f'Nombre: {self.nombre} | ' \
               f'Apellido: {self.apellido} | ' \
               f'DNI Tutor: {self.dni_tutor} | ' \
               f'Cuota: {self.cuota} | ' \
               f'Nivel: {self.nivel} '


def apellidos():
    a = ('Perez', ' Wedemeyer', 'López', 'García', 'Ramirez', 'Garaizagal', 'González',
         'Barassi', 'Brocanelli', 'Vega')

    return a


def nombres():
    n = ('Carlos', 'Felipe', 'Federico', 'Zaramay', 'Guille', 'Sofia', 'Valentina', 'Máximo', 'Lucía', 'Malena',
         'Ezequiel', 'Pedro', 'Franco')

    return n


def generate_alumno():
    dni = random.randint(39999999, 60000000)
    nombre = random.choice(nombres())
    apellido = random.choice(apellidos())
    dni_tutor = random.randint(10000000, 30000000)
    cuota = random.randint(1000, 20000)
    nivel = random.randint(1, 12)

    alumno = Alumno(dni, nombre, apellido, dni_tutor, cuota, nivel)

    return alumno


def cargar_alumno():
    dni = int(input('Ingrese el DNI del alumno: '))
    validar_dni = validar_entre(10000000, 99999999, dni)
    while not validar_dni:
        dni = int(input('Ingrese un DNI válido: '))
        validar_dni = validar_entre(10000000, 99999999, dni)

    nombre = input('Ingrese un nombre: ')
    apellido = input('Ingrese un apellido: ')
    dni_t = int(input('Ingrese el DNI del tutor: '))

    validar_dni = validar_entre(10000000, 99999999, dni_t)
    while not validar_dni:
        dni_t = int(input('Ingrese un DNI válido: '))
        validar_dni = validar_entre(10000000, 99999999, dni_t)

    cuota = int(input('Ingrese la cuota que paga el alumno'))
    nivel = int(input('A que nivel va el alumno?: '))
    validar_nivel = validar_entre(1, 12, nivel)
    while not validar_nivel:
        nivel = int(input('Ingrese un nivel válido: '))
        validar_nivel = validar_entre(1, 12, nivel)

    alumno = Alumno(dni, nombre, apellido, dni_t, cuota, nivel)
    return alumno







