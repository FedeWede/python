"""
Para chequear si un número ingresado es primo
"""
import math

primo = True
n = int(input('Ingrese un número: '))

if n % 2 == 0 and n != 2:
    primo = False
    print('Los números pares nunca son primos, asi que', n, ' no es primo')
else:
    k = int(math.sqrt(n))
    for d in range(3, k):
        r = n % d
        if r == 0:
            primo = False
if not primo:
    print('El número no es primo')
else:
    print('El número es primo!!')
