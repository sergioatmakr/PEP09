"""
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

num1=int(input("Introduce el dividendo"))
num2=int(input("Introduce el divisor"))

if num2==0:
    print("No se puede dividir entre 0")
else:
    print("El resultado es ",num1/num2)