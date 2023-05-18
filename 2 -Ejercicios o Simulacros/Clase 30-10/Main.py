from modulo import*

def principal():
    barcos = []
    op = 0
    while op != 9:

        print('blabla \n'
              '1) Crear cosos \n'
              '2) Mostrar cosos \n'
              '3) Crear archivo \n'
              '4) Mostrar el archivo ingresando el nombre \n'
              '5) Buscar por matricula y cambiar importe \n'
              '6) Buscar por nombre de propietario y mostrar \n'
              '7) Matriz \n'
              '8) Buscar por parcela \n')
        op = int(input('Opcion: '))

        if op == 1:
            barcos = crear_vector()

        if op == 2:
            suma = 0
            if len(barcos) == 0:
                print('There is no such thing')
            else:
                for i in range(len(barcos)):
                    print(barcos[i])
                    suma += barcos[i].monto
            print('-'*30)
            print(f'El total de todos los barcos es: {suma}')

        if op == 3:
            nombre = input('Que nombre le quiere poner al archivo?: ')
            crear_archivo(barcos, nombre)

        if op == 4:
            nombre = input('Que nombre de archivo desea buscar?: ')
            leer_archivo(nombre)

        if op == 5:
            matricula = input('Que matricula desea buscar. ')
            pos = buscar_por_matricula(barcos, matricula)
            if pos == len(barcos):
                print('No se encontró la matricula')
            else:
                importe_anterior = barcos[pos].monto
                importe = int(input('Que importe desea: '))
                barcos[pos].monto = importe
                print(f'Importe anterior: {importe_anterior} \n'
                      f'Registro actualizado: {barcos[pos]}')

        if op == 6:
            nombre = input('Que nombre desea buscar: ')
            barco = buscar_por_nombre(barcos, nombre)

            if not barco:
                print('No se encontró el nombre')

            else:
                print(barco)

        if op == 7:
            contadores = crear_matriz(barcos)
            mostrar_matriz(contadores)

        if op == 8:
            parcela = int(input('Que parcela desea ver: '))
            vec_parcelas = generar_vector_parcelas(barcos, parcela)

            for i in range(len(vec_parcelas)):
                print(vec_parcelas[i])


if __name__ == '__main__':
    principal()