correcto=False

while correcto != True:
    num=int(input("Introduce un número entre 1-10"))

    if num>=1 and num<=10:
        correcto=True
        print("Número correcto")
    else:
        print("Vuelve a intentarlo")    