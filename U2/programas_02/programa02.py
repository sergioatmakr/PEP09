"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.
"""

correcto=False

while correcto != True:
    num=int(input("Introduce un número entre 1-10"))

    if num>=1 and num<=10:
        correcto=True
        print("Número correcto")
    else:
        print("Vuelve a intentarlo")    