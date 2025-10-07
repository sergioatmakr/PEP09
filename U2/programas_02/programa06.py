"""
Escribe un programa que realice las siguientes operaciones:
• Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
• Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
• Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""

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