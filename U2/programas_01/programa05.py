"""
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""

num1=int(input("Introduce el primer valor"))
num2=int(input("Introduce el segundo valor"))

if num1>num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1<num2:
    print(f"El número {num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")