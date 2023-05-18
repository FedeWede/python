"""
La finalización de carga de datos se simboliza cuando el usuario pone un numero negativo
a) la sumatoria de numeros entre 50 y 100
b) Cantidad de valores par ingresados
c) Cantidad de valor impares ingresados
d) Informar si se ingreso al menos un numero 0
e) Informar si la serie ingresada fue de numeros pares e impares alternados
"""
suma = 0
cp = 0
ci = 0
ceros = False
pares_alternados = True
paridad = 3
n = int(input('Ingrese un numero: '))
while n >= 0:
    if (n > 50) and (n < 100):
        suma += n
    if n % 2 == 0:
        cp += 1
    else:
        ci += 1
    if n == 0:
        ceros = True
    if (n % 2) == paridad:
        pares_alternados = False
    paridad = n % 2
    n = int(input('Ingrese otro numero: '))

print('La suma de los numeros entre 50 y 100 es: ', suma)
print('La cantidad de numeros pares ingresados es de: ', cp)
print('La cantidad de numeros impares ingresados es de: ', ci)
if ceros is True:
    print('Se ingreso al menos un numero 0 😎')
else:
    print('No se ingreso ningun 0')
if pares_alternados is False:
    print('No se ingresaron numeros pares e impares alternadamente')
else:
    print('Se ingresaron numeros pares e impares alternadamente 😎')
