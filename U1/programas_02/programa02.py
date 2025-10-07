entero=int(6)

print(type(6))
print(type(entero))

segunda=entero

print(type(6))
print(type(segunda))

if entero is 6:
    print("Ocupan la misma posición")
else:
    print("Te has equivocado")

if segunda is 6:
    print("Ocupan la misma posición")
else:
    print("Te has equivocado")

entero="Hola"

print(type("Hola"))
print(type(entero))

print(isinstance(segunda,int))
print(isinstance(entero,str))