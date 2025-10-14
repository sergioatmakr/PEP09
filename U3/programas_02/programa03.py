"""
Escribe un programa que use los módulos platform y os para,
Mostrar el procesador donde se ejecuta el programa.
Mostrar el sistema operativo y versión donde se ejecuta el programa.
Mostrar el nombre el host donde se ejecuta el programa.
Mostrar el directorio actual.
"""

import platform, os

print(platform.processor())
print(platform.system())
print(platform.version())