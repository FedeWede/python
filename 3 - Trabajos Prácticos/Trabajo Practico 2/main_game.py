import Modulo_funciones as Mdf
from random import choice

# definir instrucciones

instrucciones_1 = "\n1. Primero el programa los tiene que conocer. Han de Ingresar sus nombres."
instrucciones_2 = "\n2. Luego tendrán que ingresar el puntaje a alcanzar para ganar."
instrucciones_3 = "\n3. Comienza la ronda: \n El jugador 1 decide si apostar a par o impar y tira 3 dados."
instrucciones_4 = "\n4. En caso de que la suma de esos 3 dados sea de la paridad que pensó el jugador 1, se le" \
                  " suma el\nvalor del dado más alto a su puntaje total. Caso contrario se le resta el dado menor." \
                  "\nEn caso de que todos los dados sean de la paridad por la que apostó el jugador 1, se le suma" \
                  " el\ndoble del dado mayor."
instrucciones_5 = "\n5. El jugador 2 realizará el mismo procedimiento. Cuando termina su turno, termina la ronda."
instrucciones_6 = "\n6. Se vuelve a jugar hasta que uno o ambos jugadores ganen (superen la puntuación para ganar)." \
                  "\nEn caso de eso suceder, gana el jugador que tenga más puntos. Si tienen los mismos puntos," \
                  "\nganará aquel que tenga la mayor cantidad de jugadas ganadas. En la ocasión de que ambos" \
                  "\ncompartan ese número, será un empate." \
                  "\n    No es necesario que se sepan todo esto, la PC lo hace sola. Ahora a jugar.\n\n"

instrucciones = tuple(
    (instrucciones_1, instrucciones_2, instrucciones_3, instrucciones_4, instrucciones_5, instrucciones_6))

# definir variables con anterioridad

puntaje_victoria = 0
eleccion_inst = 0
# bienvenida

print("¡BIENVENIDOS AL JUEGAZO DE LOS DADOS! (versión para dos jugadores)")
print("Recordatorio: las apuestas clandestinas son ilegales en Argentina.")
print("Ahora sí, a jugar. Pulse '1' para ver las instrucciones. '2' para jugar")

# elegir si mostrar instrucciones

bandera_inst = True
while bandera_inst:
    eleccion_inst = int(input("Ingrese '1' o '2': "))
    if not (eleccion_inst == 1 or eleccion_inst == 2):
        print("Ingrese bien el número por favor...")
    else:
        bandera_inst = False

# mostrar instrucciones

if eleccion_inst == 1:
    for texto in instrucciones:
        print(texto)
        input("presione Enter si ya leyó.")

# nombres

nombre_1 = input("Ingrese el nombre del jugador 1: ")
nombre_2 = input("Ingrese el nombre del jugador 2: ")

print("Ahora es turno de ingresar el puntaje necesario para ganar.")

# puntaje victoria

bandera_ingreso_puntaje = True
while bandera_ingreso_puntaje:
    puntaje_victoria = int(input("Debe ser mayor a 10: "))
    if puntaje_victoria <= 10:
        print("Ingrese bien el número por favor. Debe ser mayor a 10.\n")
    else:
        bandera_ingreso_puntaje = False
        print("Ha ingresado el número correctamente.\n")

# definir variables para proceso

empate = bandera_seguidas1 = bandera_seguidas2 = False
puntaje_t_1 = 0
puntaje_t_2 = 0
r_ganadas_1 = r_ganadas_2 = ronda_jugada = 0
tirada = cant_aciertos1 = cant_aciertos2 = 0
puntaje1 = puntaje2 = promedio_j1 = promedio_j2 = 0
contador_seguidas_1 = contador_seguidas_2 = 0

# PARTIDA

while not (puntaje_t_1 >= puntaje_victoria or puntaje_t_2 >= puntaje_victoria):

    #  juega el jugador 1 en la primera iteración del for
    aciertos1, puntaje1 = Mdf.juego(nombre_1)
    cant_aciertos1 += aciertos1

    # juega el jugador 2 en la segunda iteración del for
    aciertos2, puntaje2 = Mdf.juego(nombre_2)
    cant_aciertos2 += aciertos2

    puntaje_t_1 += puntaje1
    puntaje_t_2 += puntaje2

    # se chequea quien gana
    if puntaje1 > puntaje2:
        print('> Gana la ronda ', nombre_1, ', con ', puntaje1, ' puntos')
        r_ganadas_1 += 1
    elif puntaje2 > puntaje1:
        print('> Gana la ronda ', nombre_2, ', con ', puntaje2, 'puntos')
        r_ganadas_2 += 1
    else:
        print('Empate!')
    print('- Los puntajes hasta ahora son de: \n>', nombre_1, ':', puntaje_t_1, '\n>',
          nombre_2, ':', puntaje_t_2)

    # contadores y banderas

    if puntaje1 > puntaje2:
        contador_seguidas_1 += 1
        contador_seguidas_2 = 0
    else:
        contador_seguidas_2 += 1
        contador_seguidas_1 = 0

    if contador_seguidas_1 == 3:
        bandera_seguidas1 = True
    if contador_seguidas_2 == 3:
        bandera_seguidas2 = True

    if puntaje1 == puntaje2:
        empate = True
    ronda_jugada += 1
    promedio_j1 = puntaje_t_1 / ronda_jugada
    promedio_j2 = puntaje_t_2 / ronda_jugada

# salida ganador

mensajes_victoria = tuple((" tras reducir a cenizas a ", " tras diezmar las neuronas de ", " tras hacer polvo a "))

if puntaje_t_1 > puntaje_t_2:
    print("Gana con " + str(puntaje_t_1) + " puntos el jugador " + nombre_1 + choice(mensajes_victoria) + nombre_2)

elif puntaje_t_2 > puntaje_t_1:
    print("Gana con " + str(puntaje_t_2) + " puntos el jugador " + nombre_2 + choice(mensajes_victoria) + nombre_1)

else:

    if r_ganadas_1 > r_ganadas_2:
        print("*Gana con " + str(r_ganadas_1) + " rondas ganadas el*\n*jugador " + nombre_1 +
              "a pesar de empatar los puntos con" + nombre_2 + ".*")

    if r_ganadas_2 > r_ganadas_1:
        print("*Gana con " + str(r_ganadas_2) + " rondas ganadas el*\n*jugador " + nombre_2 +
              "a pesar de empatar los puntos con" + nombre_1 + ".*")
    else:
        print("*Tanto " + nombre_1 + " como " + nombre_2 + " han sacado los mismos*\n*puntos"
                                                           "y rondas ganadas. Es un empate.*")

# menu de opciones para estadisticas
op = 0
while op != 6:

    # ingresar opcion

    print("Ha terminado el juego!! Si te interesa, podemos mostrarte algunas estadisticas:")
    print("1- Rondas jugadas \n2- Verificar si hubo empate \n3- Puntaje promedio de cada jugador \n4- Porcentaje de "
          "aciertos de cada jugador\n5- Ver si algun jugador tuvo una racha de 3 seguidas\n 6- Terminar")
    op = int(input("> Ingrese una opcion: "))

    while 1 < op > 6:
        print("¡ERROR!")
        op = int(input("> Ingrese un numero valido!!"))

    # opcion 1
    if op == 1:
        print("> Se han jugado un total de ", ronda_jugada, " rondas")

    # opcion 2
    elif op == 2:
        if empate:
            print("> Hubo un empate!")
        else:
            print("> No hubo empate!")

    # opcion 3
    elif op == 3:
        print("> El promedio de", nombre_1, "es de", promedio_j1)
        print("> El promedio de", nombre_2, "es de", promedio_j2)

    # opcion 4
    elif op == 4:
        print("El porcentaje de aciertos de", nombre_1, "fue de: ", (cant_aciertos1 * 100 / ronda_jugada))
        print("El porcentaje de aciertos de", nombre_2, "fue de: ", (cant_aciertos2 * 100 / ronda_jugada))
        if cant_aciertos1 > cant_aciertos2 and puntaje_t_1 > puntaje_t_2:
            print(nombre_1, "Gano y ademas acerto mas veces a la paridad que", nombre_2)
        elif cant_aciertos2 > cant_aciertos1 and puntaje_t_2 > puntaje_t_1:
            print(nombre_2, "Gano y ademas acerto mas veces a la paridad que", nombre_1)
        elif cant_aciertos1 > cant_aciertos2 and puntaje_t_1 < puntaje_t_2:
            print(nombre_1, "Gano, pero acerto mas veces a la paridad", nombre_2)
        elif cant_aciertos2 > cant_aciertos1 and puntaje_t_2 < puntaje_t_1:
            print(nombre_2, "Gano, pero acerto mas veces a la paridad", nombre_1)

    # opcion 5
    elif op == 5:
        if bandera_seguidas1:
            print(nombre_1, "Gano tres veces seguidas")
        if bandera_seguidas2:
            print(nombre_2, "Gano tres veces segudias")
