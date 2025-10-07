"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue
"""

incremento=0

while incremento!=10:
    incremento+=1
    if incremento%2==1:
        continue
    print(incremento)

incremento=0

while incremento!=10:
    incremento+=1
    if incremento%2==0:      
        print(incremento)

for i in range(2,11,2):
    print(i)

for i in range(1,11):
    if i%2==1:
        continue
    print(i)
