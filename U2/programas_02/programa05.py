correcto=False

while not correcto:
    num=int(input("Introduce un número entre 1-10 para imprimir"))
    if num>=1 and num<=10:
        correcto=True    

for i in range(0,num):
    print(i+1)