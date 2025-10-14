# ===============================================
# conversiones.py
# Módulo con funciones para conversión de números
# ===============================================

def a_binario(n):
    """
    Devuelve la representación binaria de un número entero como cadena.
    Ejemplo: a_binario(10) → '0b1010'
    """
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    return bin(n)  # Devuelve una cadena tipo '0b1010'


def a_hexadecimal(n):
    """
    Devuelve la representación hexadecimal de un número entero como cadena.
    Ejemplo: a_hexadecimal(255) → '0xff'
    """
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    return hex(n)  # Devuelve una cadena tipo '0xff'


def a_entero(texto):
    """
    Convierte una cadena numérica en un número entero.
    Controla los errores si el texto no es un número válido.
    Ejemplo: a_entero('123') → 123
    """
    try:
        return int(texto)
    except ValueError:
        return "Error: El texto no representa un número entero válido."
