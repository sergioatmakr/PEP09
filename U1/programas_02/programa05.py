num1=float(input("Dime el número 1"))
num2=float(input("Dime el número 2"))

suma=num1+num2
resta=num1-num2
multi=num1*num2
div=num1/num2 if num2!=0 else "no se puede dividir entre 0"
mod=num1%num2 if num2 != 0 else "No se puede calcular el módulo con 0"
potencia=num1**num2

print(f"La suma de {num1} + {num2} = {suma}")
print(f"La resta de {num1} - {num2} = {resta}")
print(f"La multiplicación de {num1} * {num2} = {multi}")
print(f"La división de {num1} / {num2} = {div}")
print(f"El módulo de {num1} % {num2} = {mod}")
print(f"La potencia de {num1} ** {num2} = {potencia}")