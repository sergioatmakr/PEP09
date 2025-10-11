"""
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
• calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
retorna su área.
• calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
del triangulo y retorna su área.
• calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
del rectángulo y retorna su área.
• mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
• main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
correspondiente en función de la opción seleccionada.
• opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
sea mayor que 0 y una vez que ha validado el radio llamará a la función
calcular_area_circulo.
• opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
a la función calcular_area_triangulo.
• opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
calcular_area_rectangulo.
"""

def main():
    correcto=False
    while not correcto:
        mostrar_menu()
        opcion=int(input())
        if opcion>=1 and opcion<=4:
            correcto=True
    match opcion:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            return 4


def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
    print("Introduce una opción (1-4):")
    
        
def calcular_area_circulo(radio):
    area= 3,14*radio**2
    return print(f"El area del circulo es 3,14*{radio}^2 = {area}")

def opcion1():
    correcto=False
    while not correcto:
        radio=int(input("Introduce el radio de tu circulo"))
        if radio>0:
            correcto=True
    calcular_area_circulo (radio)

def calcular_area_triangulo(base,altura):
    return print(f"El area del triangulo es ({base}*{altura})/2={(base*altura)/2}")

def opcion2():
    correcto=False
    while not correcto:
        base=int(input("Introduce la base de tu triangulo"))
        if base>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")

    correcto=False
    while not correcto:
        altura=int(input("Introduce la altura de tu triangulo"))
        if altura>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")
    
    calcular_area_triangulo(base,altura)

def calcular_area_rectangulo(base,altura):
    return print(f"El area del rectangulo es {base}*{altura}={base*altura}")
    
def opcion3():
    correcto=False
    while not correcto:
        base=int(input("Introduce la base de tu rectangulo"))
        if base>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")

    correcto=False
    while not correcto:
        altura=int(input("Introduce la altura de tu rectangulo"))
        if altura>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")
    
    calcular_area_rectangulo(base,altura)


opcion=main()

while opcion !=4:
    opcion=main()