entero=int(input("Introduce un número entero: "))
decimal=float(input("Introduce un número decimal: "))
cadena=str(input("Introduce una cadena de texto: "))

print(f"{entero}, {type(entero)}")
print(f"{decimal}, {type(decimal)}")
print(f"{cadena}, {type(cadena)}")

enteroCorrecto= bool(entero is int)
decimalCorrecto= bool(decimal is int)
cadenaCorrecto= bool(cadena is int)

print(isinstance(entero,int))
print(isinstance(decimal,float))
print(isinstance(cadena,str))