"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

num_jugadores=int(input("Introduce el número de jugadores que van a jugar contra la banca"))
for i in range(0,num_jugadores):
    banca=random.randrange(17,22)
    jugador=random.randrange(1,6)
    respuesta="Si"
    while respuesta=="Si" and jugador<=21:
        print("El valor de tu mano es ",jugador)
        print("El valor de la banca es ",banca)
        respuesta=input("¿Quiere pedir otra carta?(Introduzca Si en caso afirmativo)")
        jugador+=random.randrange(1,6)

    if jugador>21:
        print("Te has pasado gana la banca")   
    elif jugador>banca:
        print("Enhorabuena has ganado a la banca") 
    else:
        print("Has perdido")