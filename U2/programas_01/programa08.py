import random
jugador11=random.randrange(1,7)
jugador12=random.randrange(1,7)
jugador21=random.randrange(1,7)
jugador22=random.randrange(1,7)
igual=True

if jugador11+jugador12>jugador21+jugador22:
    print(f"El jugador 1 ha ganado obteniedno una puntuación de {jugador11+jugador12} y j2 {jugador21+jugador22}")
elif jugador11+jugador12<jugador21+jugador22:
    print(f"El jugador 2 ha ganado obteniedno una puntuación de {jugador21+jugador22} y j2 {jugador11+jugador12}")
else:
    if jugador11>jugador12:
        if jugador11>jugador21 and jugador11>jugador22:
            print("La tirada mas grande es del jugador 1 y es de ",jugador11)
            igual=False
    else:
        if jugador12>jugador21 and jugador12>jugador22:
            print("La tirada mas grande es del jugador 1 y es de ",jugador12)
            igual=False

    if jugador21>jugador22:
        if jugador21>jugador11 and jugador21>jugador12:
            print("La tirada mas grande es del jugador 2 y es de ",jugador21)
            igual=False
    else:
        if jugador22>jugador11 and jugador22>jugador12:
            print("La tirada mas grande es del jugador 2 y es de ",jugador22)
            igual=False
    if igual:
        print("Ambos jugadores tienen la misma puntuación global y su mayor tirada es igual j1")


