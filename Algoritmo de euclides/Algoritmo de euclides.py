"""
 Sacar el mcd entre dos números


a = int(input('Introducir el número mayor: '))
b = int(input('Introducir el número menor: '))

resto = a % b

while resto != 0:
    resto_2 = b % resto
    b = resto
    resto = resto_2
print('El MCD es: ', b)
"""


class Libros:
    def __init__(self, codigo, titulo, genero, idioma, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


libros = []
for i in range(10):
    libros.append(Libros(10, 'Pepe', 1, 1, 1000))


def busqueda_de_mayor(libros):
    idi_selec = int(input("Ingrese el idioma que desea para buscar el libro de mayor precio: "
                          "\n1- Español"
                          "\n2- Inglés"
                          "\n3- Francés"
                          "\n4- Italiano"
                          "\n5- Otros"
                          "\n--> "))
    while 1 > idi_selec < 5:
        idi_selec = int(input("Ingrese el idioma que desea para buscar el libro de mayor precio: "
                              "\n1- Español"
                              "\n2- Inglés"
                              "\n3- Francés"
                              "\n4- Italiano"
                              "\n5- Otros"
                              "\n--> "))

    idi_selec = idi_selec - 1
    libro_precio_may = None

    for i in range(len(libros)):
        if int(libros[i].idioma) == idi_selec:
            if libro_precio_may is None or int(libros[i].precio) > int(libro_precio_may.precio):
                libro_precio_may = libros[i]

    return libro_precio_may, idi_selec


prueba_1, prueba_2 = busqueda_de_mayor(libros)
print(prueba_1, prueba_2)