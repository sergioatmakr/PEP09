"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.
"""

correcto=False

while not correcto:
    num=int(input("Introduce un número entre 1-10 para imprimir"))
    if num>=1 and num<=10:
        correcto=True    

for i in range(0,num):
    print(i+1)