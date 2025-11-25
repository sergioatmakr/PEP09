import random

def generar_enemigo():
    nombres=["Hydra","Kraken","Minotauro","Gorgona","Titan"]
    nombre=random.choice(nombres)
    conocimiento=random.randrange(1,11)
    energia=random.randrange(1,6)

    return nombre,conocimiento,energia

def ataque_enemigo(conocimiento,energia):
    return conocimiento*energia*random.randrange(1,4)

def mostrar_enemigo(nombre,conocimiento,energia):
    print(f"{nombre} tiene {conocimiento} puntos de conocimiento y {energia} puntos de energia")