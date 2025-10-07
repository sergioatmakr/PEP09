"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""

#Versión break
total=0
media=0
while True:
    num=int(input("Introduce un número (0 para salir)"))
    total+=num
    media+=1
    if num==0:
        break
print(f"La suma total es {total}")
print(f"La media es {total/media}")

#Versión sin break

num=-1
total=0
media=0
while num!=0:
    num=int(input("Introduce un número (0 para salir)"))
    total+=num
    media+=1

print(f"La suma total es {total}")
print(f"La media es {total/media}")