#Se pueden obtener de la dirección pypi.org.
#Para instalar el paquete "Cowsay" escribir en la terminal: "pip install cowsay".

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
