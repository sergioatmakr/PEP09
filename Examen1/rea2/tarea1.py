import random

vidas=3
puntos=0
nivel=1

while vidas!=0:
    """Imprimir la vida puntos y nivel"""
    print(f"Jugador tienes {vidas} vidas {puntos} puntos y eres de nivel {nivel}")
    """Elegir una opción de los diferentes ataques"""
    print("Elige un tipo de ataque")
    print("1. Ataque de fuerza")
    print("2. Ataque de precisión")
    print("3. Ataque de riesgo")
    try:
        opcion=int(input())
        """En función de la opción elegida generar diferentes número aleatorios"""
        match opcion:
            case 1:
                jugador=random.randrange(5,11)
                maquina=random.randrange(3,10)
                if jugador>maquina:
                    puntos+=1
                elif jugador==maquina:
                    print("empate no pasa nada")
                    empate=True    
                else:
                    vidas-=1
                    derrota=True 
            case 2:
                jugador=random.randrange(3,9)
                maquina=random.randrange(2,10)
                if jugador>maquina:
                    puntos+=1
                elif jugador==maquina:
                    print("empate no pasa nada")
                    empate=True     
                else:
                    vidas-=1
                    derrota=True 
            case 3:
                jugador=random.randrange(1,11)
                maquina=random.randrange(1,9)
                if jugador>maquina:
                    puntos+=1
                elif jugador==maquina:
                    print("empate no pasa nada")
                    empate=True     
                else:
                    vidas-=1
                    derrota=True
            case _:
                print("Introduce un numero correcto")         
    except ValueError:
        print("Tienes que introducir una de las 3 opciones con un numero correcto")
    
     
    """Hacer que cada tres puntos ganes 1 vida cuando las vidas no están al máximo"""            
    if(puntos%3==0 and puntos!=0 and not empate and not derrota) :
        if(vidas!=3):
            vidas+=1
        nivel+=1
    empate=False
    derrota=False
print(f"La partida ha terminado tu puntuación es de {puntos} y has terminado con el nivel {nivel} ")
          

