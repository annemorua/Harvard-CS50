#todo Hay otro método llamado "re.match" que sabe que está iniciando desde el principio.
#todo También "re.fullmatch" en el cual no hay que especificar ni inicio ni final (^$).

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")


     ### PARA PERMITIR LOS PUNTOS DELANTE DEL DOMAIN ###

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")
