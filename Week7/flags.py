#todo re.IGNORECASE
#todo re.MULTILINE
#todo re.DOTALL

import re

email = input("What's your email? ").strip()

#re.IGNORECASE ignora si el input está en mayúscula o minúscula.
if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE):
    print("Valid")

else:
    print("Invalid")
