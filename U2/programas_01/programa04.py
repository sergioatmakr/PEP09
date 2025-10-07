num=int(input("Introduce un número entre 1-10"))

match num:
    case 0 | 1 | 2 | 3 | 4:
        print("Insuficiente")
    case 5 | 6:
        print("Bien")
    case 7 | 8 | 9:
        print("Notable")
    case 10:
        print("Sobresaliente")
    case _:
        print("Introduce una nota correcta")
