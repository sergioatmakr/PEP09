from os import strerror

try:
    fichero = open("hola.txt", "rt", encoding="utf-8")

    try:
        contenido = fichero.readlines()
        print(contenido)

    except Exception as exc:
        print("ERROR", strerror(exc.errno))
        
    finally:
        fichero.close()

except Exception as exc:
    print("ERROR", strerror(exc.errno))
