"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra.
"""

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