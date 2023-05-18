import random
from registro_Libros import *


def generar_arreglo_aleatorio(n, libros):  # agrega n libros generados aleatoriamente a un array
    opciones_titulos_1 = ('Harry Potter', 'Percy Jackson', 'El Loco', 'El Guille', 'Zaramay', 'Tu familia', 'Sonic',
                          'Menem', 'Mi amigo Ezequiel')
    opciones_titulos_2 = ('Sus Secuaces', 'Sus Múltiples amigos', 'Su Perro Tito', 'La Piedra Filosofal', 'Su Celular',
                          'Su Amigo Pepe', 'Sus Enemigos')

    for i in range(n):
        codigo = generar_isbn()  # genera isbn aleatorio, válido
        titulo = random.choice(opciones_titulos_1) + ' y ' + random.choice(opciones_titulos_2)  # Inventa un titulo
        genero = random.randint(0, 9)  # Género aleatorio
        idioma = random.randint(1, 5)  # Idioma aleatorio
        precio = random.randint(5000, 8000)  # Precio entre $5000 y $8000

        libros.append(Libros(codigo, titulo, genero, idioma, precio))

    print(f'Se han agregado {n} libros!')
    return libros


def generar_isbn():  # genera un isbn con numeros aleatorios, luego se valida si es un isbn válido y si no lo es se
    # vuelve a generar hasta que lo sea
    isbn = None
    isbn_valido = False
    while not isbn_valido:
        isbn_list = []
        for i in range(10, 0, -1):
            num = random.randint(0, 9)  # crea un isbn totalmente aleatorio
            isbn_list.append(num)
        isbn = f'{isbn_list[0]}{isbn_list[1]}-{isbn_list[2]}{isbn_list[3]}{isbn_list[4]}{isbn_list[5]}-{isbn_list[6]}' \
               f'{isbn_list[7]}-{isbn_list[8]}{isbn_list[9]}'  # concatena el número isbn en un string con guiones
        isbn_valido = validar_ISBN_sin_prints(isbn)  # aprovecha la función validadora

    return isbn


def verificar_num(car):  # verifica si un caracter es un numero
    numeros_txt = "0123456789"
    es_num = False
    for i in numeros_txt:
        if i == car:
            es_num = True
            break
    return es_num


def validar_ISBN_sin_prints(isbn):  # función validadora para cuando el ISBN se quiere generar automáticamente
    validacion = True

    cant_grup = 0  # cantidad de grupos
    numero_final = 0  # el numero que vamos a dividir por 11
    cant_num = 0  # la cantidad de numeros
    prev_pos_is_num = False
    for i in isbn:
        if verificar_num(i):  # hace operaciones con numeros
            numero_final += (10 - cant_num) * int(i)
            # print(numero_final)
            cant_num += 1
            prev_pos_is_num = True

        elif i == '-':
            if cant_num == 10:  # si el guion esta al final
                validacion = False

            if not prev_pos_is_num:  # hay dos guiones juntos
                validacion = False

            prev_pos_is_num = False
            cant_grup += 1

        else:
            # es un caracter ni numero ni guion
            validacion = False

    # verificacion final
    if numero_final % 11 != 0:
        validacion = False
    if cant_num != 10:
        validacion = False

    if cant_grup != 3:
        validacion = False

    return validacion


def validar_ISBN(isbn):  # verificar que el isbn sea valido cuando es cargado por teclado y proporciona feedback de
    # porqué el ISBN no es válido.
    validacion = True

    cant_grup = 0  # cantidad de grupos
    numero_final = 0  # el numero que vamos a dividir por 11
    cant_num = 0  # la cantidad de numeros
    prev_pos_is_num = False
    for i in isbn:
        if verificar_num(i):  # hace operaciones con numeros
            numero_final += (10 - cant_num) * int(i)
            # print(numero_final)
            cant_num += 1
            prev_pos_is_num = True

        elif i == '-':
            if cant_num == 10:  # si el guion esta al final
                validacion = False
                print("\nHa colocado un guion al final")

            if not prev_pos_is_num:  # hay dos guiones juntos
                print("\nHa colocado dos guiones seguidos")
                validacion = False

            prev_pos_is_num = False
            cant_grup += 1

        else:
            # es un caracter ni numero ni guion
            print("\nUno de los caracteres no es ni numero ni guion.")
            validacion = False

    # verificacion final
    if numero_final % 11 != 0:
        validacion = False
        print("\nNo son numeros validos.")
    if cant_num != 10:
        validacion = False
        print("\nNo tiene 10 numeros.")

    if cant_grup != 3:
        validacion = False
        print("\nNo tiene 4 grupos.")

    return validacion


def ingresar_datos_libro():  # carga libros a un array de manera manual
    print("----Ingreso de datos de forma manual----")

    cod_isbn = input("Ingrese el codigo ISBN (favor de ingresarlo correctamente): ")
    while not validar_ISBN(cod_isbn):
        print("Codigo no valido. Ingrese otra vez.")
        cod_isbn = input("Ingrese el codigo ISBN (favor de ingresarlo correctamente): ")

    # ingresar y validad el titulo
    titulo = input("Ingrese el titulo del libro: ")
    while len(titulo) == 0:
        print("Titulo vacio. Ingrese otra vez.")
        titulo = input("Ingrese el titulo del libro: ")

    # ingresar y validar el genero
    genero = int(input("Ingrese el genero del libro (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, \n"
                       "5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros) : "))
    while genero < 0 or genero > 9:
        print("Ingrese un genero dentro del rango (0-9)")
        genero = int(
            input("Ingrese el genero del libro (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, \n"
                  "5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros) : "))

    # ingresar y validar el idioma
    idioma = int(input("Ingrese el idioma del libro (1: español, 2: inglés, 3: francés, 4: italiano, 5: otros): "))
    while idioma < 1 or idioma > 5:
        print("Ingrese un idioma dentro del rango (1-5)")
        idioma = int(input("Ingrese el idioma del libro (1: español, 2: inglés, 3: francés, 4: italiano, 5: otros): "))

    # ingresar y validar precio
    precio = int(input("Ingrese el precio del libro: "))
    while precio < 0:
        print("Ingrese un precio correctamente.")
        precio = int(input("Ingrese el precio del libro: "))

    return Libros(cod_isbn, titulo, genero, idioma, precio)


def mostrar_libros(libros):  # muestra los libros en el sistema de a uno por linea
    idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad",
               "Gastronomía", "Infantíl", "Otros"]

    # Ordena los libros alfabéticamente
    bubble_sort_alfabetico(libros)

    # Muestra los libros a razón de uno por linea
    for i in range(len(libros)):
        print(
            f'{libros[i].codigo} | {libros[i].titulo} | {idiomas[libros[i].idioma - 1]} | {generos[libros[i].genero]} '
            f'| ${libros[i].precio}')


def bubble_sort_alfabetico(v):  # bubble sort para ordenar alfabéticamente por título
    n = len(v)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if v[j].titulo > v[j + 1].titulo:
                ordenado = False
                v[j], v[j + 1] = v[j + 1], v[j]
        if ordenado:
            break


def bubble_sort_precio(v):  # bubble sort para ordenar por precio mayor a menor
    n = len(v)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if v[j].precio < v[j + 1].precio:
                ordenado = False
                v[j], v[j + 1] = v[j + 1], v[j]
        if ordenado:
            break


def contador_de_generos(libros):  # contar libros por género

    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad",
               "Gastronomía", "Infantíl", "Otros"]

    cont_genero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mayor_genero = genero_popular = 0
    nom_may_genero = ""

    for i in range(len(libros)):  # contar los libros en un vector de conteo
        cont_genero[libros[i].genero] += 1
    print("La cantidad de libros que hay por genero son: ")

    for i in range(10):  # determinar el género con más libros
        print(f"-{generos[i]}: {cont_genero[i]}")
        if cont_genero[i] > mayor_genero:
            nom_may_genero = generos[i]
            genero_popular = i
            mayor_genero = cont_genero[i]

    # mostrar resultado
    print(f"El genero con mayor cantidad de libros es el de {nom_may_genero}")

    return genero_popular  # return del género popular para usar en el punto 6


def busqueda_de_mayor(libros):  # busca el libro con mayor precio de un idioma en específico

    idi_selec = int(input("Ingrese el idioma que desea para buscar el libro de mayor precio: "
                          "\n1- Español"
                          "\n2- Inglés"
                          "\n3- Francés"
                          "\n4- Italiano"
                          "\n5- Otros"
                          "\n--> "))
    while 1 > idi_selec < 5:  # validador
        idi_selec = int(input("Ingrese el idioma que desea para buscar el libro de mayor precio: "
                              "\n1- Español"
                              "\n2- Inglés"
                              "\n3- Francés"
                              "\n4- Italiano"
                              "\n5- Otros"
                              "\n--> "))

    libro_precio_may = None

    for i in range(len(libros)):  # selecciona el libro de mayor precio
        if int(libros[i].idioma) == idi_selec:
            if libro_precio_may is None or int(libros[i].precio) > int(libro_precio_may.precio):
                libro_precio_may = libros[i]

    return libro_precio_may, idi_selec


def buscar_por_isbn(vector, codigo):  # busca por isbn y corta cuando encuentra el primero

    for i in range(len(vector)):
        if codigo == vector[i].codigo:
            return vector[i]

    return False


def consulta_de_un_genero(libros, genero):  # devuelve los libros del género más popular determinado en el punto 3
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad",
               "Gastronomía", "Infantíl", "Otros"]
    idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]

    if genero == 10:
        print('Primero debe usar la opción 4!')
        return

    libros_del_genero = []  # se guardan los líbros del género elegido en este vector
    for i in range(len(libros)):
        if libros[i].genero == genero:
            libros_del_genero.append(libros[i])

    bubble_sort_precio(libros_del_genero)  # ordena los libros por su precio

    print(f'Los libros del género "{generos[genero]}" son: ')
    for j in range(len(libros_del_genero)):
        print(f'{libros_del_genero[j].codigo} | {libros_del_genero[j].titulo} | '
              f'{idiomas[libros_del_genero[j].idioma - 1]} | {generos[genero]} | '
              f'${libros_del_genero[j].precio}')


def buscar_grupo_de_libros(libros):  # busca n libros según su ISBN utilizando la función para buscar

    n = int(input('Cuantos libros desea buscar?: '))
    suma = 0
    libros_buscados = [] * n  # en este vector se guardarán los libros solicitados
    no_encontrados = []  # aquí se guardan los libros que no se encuentran
    for i in range(n):
        codigo = input(f'Cargue el codigo ISBN del libro {i + 1}: ')
        codigo_valido = validar_ISBN(codigo)  # valida si el código ISBN escrito es correcto
        while not codigo_valido:
            codigo = input('Por favor cargue un código correcto: ')
            codigo_valido = validar_ISBN(codigo)

        libro_buscado = buscar_por_isbn(libros, codigo)  # busca el libro
        if libro_buscado is False:  # si no lo encuentra suma su código a un vector
            no_encontrados.append(codigo)

        else:  # si lo encuentra suma el libro a un vector con los resultados
            libros_buscados.append(libro_buscado)

    # muestra los resultados
    print('Los libros encontrados son: ')
    for f in range((len(libros_buscados))):
        suma += libros_buscados[f].precio
        print(f'{libros_buscados[f].titulo} | ${libros_buscados[f].precio}')
    print(f'El total a pagar es de ${suma}')

    if len(no_encontrados) != 0:
        print('Los libros que no se encontraron son:')
        for k in range(len(no_encontrados)):
            print(f'Código: {no_encontrados[k]}')
