"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""

par=int(input("Introduce un número par"))
if par%2 !=0:
    print("El número no es par")
else:
    impar=int(input("Introduce un número impar"))
    if impar%2!=1:
        print("El número no es impar")