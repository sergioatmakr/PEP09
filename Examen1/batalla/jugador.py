import random

def ataque_jugador(conocimiento,energia):
    return conocimiento*energia*random.randrange(1,4)

def mostrar_jugador(nombre,conocimiento,energia):
    print(f"Jugador tu nombre es {nombre} tienes {conocimiento} puntos de conocimiento y {energia} puntos de energia")