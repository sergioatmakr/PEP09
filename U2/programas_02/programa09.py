"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random
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