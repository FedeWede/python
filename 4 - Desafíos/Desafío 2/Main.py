def sucesion(num):
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            orbita.append(int(num))
        else:
            num = num * 3 + 1
            orbita.append(int(num))


suma = 0
n = int(input('Ingrese un numero: '))
orbita = [n]
sucesion(n)

for numero in orbita:
    suma += numero

print('La órbita es: \n', orbita)
print('La órbita tiene ', len(orbita), 'elementos')
print('El promedio de la órbita es de: ', suma / (len(orbita)))
print('El máximo número de la órbita es', max(orbita))
