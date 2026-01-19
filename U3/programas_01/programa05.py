"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""
# Variable global
def mostrar():
    print(a)
    return
a = 5
mostrar()
print(a)

# Variable no local
def mostrar():
    def sub_mostrar():
        print(a)
        return
    a = 3
    sub_mostrar()
    print(a)
    return
a = 4
mostrar()
print(a)

#Variable local
def mostrar():
    a = 2
    print(a)
mostrar()
print(a) # Error, la variable local a solo es "visibe/existe"
#dentro de la funcion.