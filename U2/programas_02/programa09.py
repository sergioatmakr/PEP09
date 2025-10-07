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
