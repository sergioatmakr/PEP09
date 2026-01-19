# ===============================================
# imports de la librería estándar
# ===============================================
# (No se necesitan módulos de la biblioteca estándar en este caso.)

# ===============================================
# imports de librerías de terceros
# ===============================================
# (No se usan librerías externas.)

# ===============================================
# imports de módulos propios
# ===============================================
import enemigo
import jugador

# ===============================================
# Función principal
# ===============================================
def main():
    """"""
    try:
        nombre=str(input("Introduce tu nombre"))
    except ValueError:
        print("Introduce un nombre")


    correcto=False

    while not correcto:
        try:
            conocimiento=int(input("Introduce tu conocimiento 1-10"))
            if(conocimiento>=1 and conocimiento<=10):
                correcto=True
        except ValueError:
            print("Introduce un valor entero")

    correcto=False

    while not correcto:
        try:
            energia=int(input("Introduce tu energia 1-5"))
            if(energia>=1 and energia<=5):
                correcto=True
        except ValueError:
            print("Introduce un valor entero")

    """"""
    nombreEnemigo,conocimientoEnemigo,energiaEnemigo=enemigo.generar_enemigo()        

    """"""
    for i in range(0,3):
        magiaJugador=jugador.ataque_jugador(conocimiento,energia)
        magiaEnemigo=enemigo.ataque_enemigo(conocimientoEnemigo,energiaEnemigo)

        if(magiaJugador==magiaEnemigo):
            print("Empate")
        elif(magiaJugador>magiaEnemigo):
            energiaEnemigo-=1
        else:
            energia-=1
        enemigo.mostrar_enemigo(nombreEnemigo,conocimientoEnemigo,energiaEnemigo)
        jugador.mostrar_jugador(nombre,conocimiento,energia)

    if(energia>energiaEnemigo):
        print("El ganador es el jugador")
        jugador.mostrar_jugador(nombre,conocimiento,energia)
    elif(energiaEnemigo>energia):
        print("El ganador es el enemigo")
        enemigo.mostrar_enemigo(nombreEnemigo,conocimientoEnemigo,energiaEnemigo)
    else:
        print("El jugador y el enemigo han empatado")
        jugador.mostrar_jugador(nombre,conocimiento,energia)
        enemigo.mostrar_enemigo(nombreEnemigo,conocimientoEnemigo,energiaEnemigo)




# ===============================================
# Bloque de ejecución principal
# ===============================================
if __name__ == "__main__":
    main()
