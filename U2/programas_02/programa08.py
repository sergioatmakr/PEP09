import random

num_secreto=random.randrange(1,21)
respueta=False
while not respueta:
    num=int(input("Intenta adivinar el número secreto entre 1-20"))

    if num != num_secreto:
        if num_secreto>num:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")