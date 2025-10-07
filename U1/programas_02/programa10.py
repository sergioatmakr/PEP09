numero = int(input("Introduce un número de dos cifras: "))


if numero < 10 or numero > 99:
    print("Por favor, introduce un número de dos cifras.")
else:
    decenas = numero // 10      
    unidades = numero % 10     
  
    invertido = unidades * 10 + decenas

   
    print("El número invertido es:", invertido)