#todo [] set of characters
#todo [^] complementing the rest

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")

else:
    print("Invalid")


      ### PARA ESPECIFICAR LO QUE QUEREMOS ANTES DEL @ ###

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid")

else:
    print("Invalid")
