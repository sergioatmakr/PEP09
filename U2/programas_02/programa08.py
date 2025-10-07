import random
#Versión sin intentos
num_secreto=random.randrange(1,21)
respueta=False
while not respueta:
    num=int(input("Intenta adivinar el número secreto entre 1-20"))

    if num != num_secreto:
        if num_secreto>num:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")
    else:
        respueta=True
        print("Enhorabuena has encontrado el numero secreto ",num_secreto)

#Versión con 3 intentos
num_secreto=random.randrange(1,21)
respueta=False
num_intentos=0
while not respueta and num_intentos!=3:
    num=int(input("Intenta adivinar el número secreto entre 1-20"))

    if num != num_secreto :
        if num_secreto>num:
            print("El número secreto es mayor")
            num_intentos+=1
            print("Te quedan ",3-num_intentos," intentos")
        else:
            print("El número secreto es menor")
            num_intentos+=1
            print("Te quedan ",3-num_intentos," intentos")
    else:
        respueta=True
        print("Enhorabuena has encontrado el numero secreto ",num_secreto)
if num_intentos==3 and not respueta:
    print("Lo siento te has quedado sin intentos")