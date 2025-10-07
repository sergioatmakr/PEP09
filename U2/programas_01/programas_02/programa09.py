import random
maquina=random.randrange(1,4)
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
jugador=int(input("Seleccione una opción (1, 2 o 3):"))

if(jugador>=1 and jugador<=3):
    match jugador:
        case 1:
            if maquina==1:
                print("Empate")
            elif maquina==2:
                print("Derrota")
            else:
                print("Victoria")
        case 2:
            if maquina==1:
                print("Victoria")
            elif maquina==2:
                print("Empate")
            else:
                print("Derrota")
        case 3:
            if maquina==1:
                print("Derrota")
            elif maquina==2:
                print("Victoria")
            else:
                print("Empate")
        case _:
            print("Tienes que elegir entre 1,2 o 3")



