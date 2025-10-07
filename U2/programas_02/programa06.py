repetir=True
while repetir:
    correcto=False

    while not correcto:
        num=int(input("Introduce un número entre 1-10 para imprimir"))
        if num>=1 and num<=10:
            correcto=True  

    for i in range(0,10):
        print(i+1,"*",num,"=",num*(i+1))

    respuesta=str(input("En caso de querer imprimir mas tablas introduzca Si"))    

    if respuesta=="Si":
        repetir=True
    else:
        repetir=False