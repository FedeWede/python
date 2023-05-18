"""
Cargar x cantidad de barcos y determinar si son veleros o lanchas

1- Total anual de veleros y total anual de lanchas
2- Nombre del velero que mas paga por mes y el valor de su cuota
3- Valor promedio de la cuota entre barcos y veleros
4- Porcentaje de la cuota de los veleros y los lanchas por el total por mes
"""

mayor = 0
SCV = 0
SCL = 0
C = int(input('Ingrese la cantidad de barcos que va a controlar: '))
bp = 'No se ingresaron veleros'

for i in range(C):
    barco = input('Ingrese el nombre del barco: ')
    tipo = int(input('Ingrese el tipo de embarcacion (1 - Veleros | 2 - Lanchas) \n'
                     'Su respuesta:  '))
    cuota = float(input('Ingrese el monto de su cuota: '))
    if tipo == 1:
        SCV += cuota
        if cuota > mayor:
            mayor = cuota
            bp = barco
    else:
        SCL += cuota
if C < 0 or None:
    print('No se cargaron barcos')
else:
    promedio = (SCL + SCV) / C
    porcentaje_lancha = SCL * 100 / (SCL + SCV)
    porcentaje_velero = SCV * 100 / (SCL + SCV)

    print('El total anual que se gana con los veleros es de: ', SCV * 12,
          '\n El total anual que se gana con las lanchas es de: ', SCL * 12,
          '\n El velero que mas paga por mes es: ', bp, 'y paga', mayor,
          '\n El valor promedio de la cuota entre barcos y veleros es de: ', promedio,
          '\n El porcentaje de cuota de los veleros con respecto al mes es de: ', porcentaje_velero,
          '\n El porcentaje de cuota de las lanchas con respecto al mes es de: ', porcentaje_lancha)
