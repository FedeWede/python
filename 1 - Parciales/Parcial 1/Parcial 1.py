'''
Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

1.)    Ingrese tres cantidades que corresponden a las ventas de tres sucursales de una empresa informática, y cargue
también el nombre de cada sucursal. Muestre el nombre de la sucursal con menor cantidad de ventas.
Informe si el promedio de las tres cantidades fue mayor a 100. En caso contrario informar "No cumplió la condición".

2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia
finaliza cuando se ingresa un cero. Determine el porcentaje de números que sean pares y mayores a 50 respecto
al total de números ingresados. Informe si el porcentaje calculado se encuentra incluido está entre los
valores x e y (que también deben ser cargados por teclado). En caso contrario informar que el porcentaje
no se encuentra dentro del rango especificado.

3.)    Terminar el programa.
'''

__author__ = 'Federico Wedemeyer, 1K6, 90328'

# Menu de opciones
op = 0
while op != 3:
    print('-'*25)
    print('Ejercicio del primer parcial')
    print('-' * 25)
    print('Elija una de las opciones:')
    print('> 1: Control de ventas')
    print('> 2: Secuencia de numeros')
    print('> 3: Salir')
    op = int(input('Ingrese una opcion: '))


# Opcion 1
    if op == 1:
        s1 = input('Ingrese el nombre de la primer sucursal: ')
        v1 = int(input('Ingrese la cantidad vendida en dicha sucursal: '))
        s2 = input('Ingrese el nombre de la segunda sucursal: ')
        v2 = int(input('Ingrese la cantidad vendida en dicha sucursal: '))
        s3 = input('Ingrese el nombre de la tercer sucursal: ')
        v3 = int(input('Ingrese la cantidad vendida en dicha sucursal: '))

        if v1 < v2 and v1 < v3:
            smenor = s1
            vmenor = v1
        elif v2 < v1 and v2 < v3:
            smenor = s2
            vmenor = v2
        else:
            smenor = s3
            vmenor = v3
        print('> La sucursal que menos vendio fue', smenor, 'que solo vendio', vmenor)
        if (v1+v2+v3)/3 > 100:
            print('> El promedio fue mayor a 100')
        else:
            print('> No supero la condicion')
        input('Presione ENTER para continuar...')

# Opcion 2
    par = numero = 0
    if op == 2:
        num = int(input('Ingrese un numero, 0 para salir: '))
        while num != 0:
            numero += 1
            if num > 50 and (num % 2 == 0):
                par += 1
            num = int(input('Ingrese un numero, 0 para salir: '))
        porcentaje = (par * 100 / numero)
        x = int(input('Ingrese el primer valor del rango: '))
        y = int(input('Ingrese el segundo valor del rango: '))
        if porcentaje >= x and porcentaje <= y:
            print('> El porcentaje se encuentra dentro del rango especificado')
        else:
            print('> El porcentaje no se encuentra dentro del rango especificado')
        input('Presione ENTER para continuar...')

# Terminar (opcion 3)
    if op == 3:
        print('Gracias por utilizar el programa!')

    if op != 1 and op != 2 and op != 3:
        print('> Ingrese una opcion valida')
        input('Presione ENTER para continuar...')
