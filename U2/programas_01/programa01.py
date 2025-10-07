"""
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
"""

par=int(input("Introduce un número par"))
impar=int(input("Introduce un número impar"))

if par%2 !=0 or impar%2!=1:
    print("Algunos de los dos números introducidos son incorrectos")
else:
    print("Los valores introducidos son correctos")