#todo ^ matches the start of the string
#todo $ matches the end of the string or just before the newline at the end of the string

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.com$", email):
    print("Valid")

else:
    print("Invalid")
