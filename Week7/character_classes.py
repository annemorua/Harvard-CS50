#todo \d decimal digit
#todo \D not a decimal digit
#todo \s whitespace characters
#todo \S not a whitespace characters
#todo \w hace esto [a-zA-Z0-9_]
#todo \W no hace lo de arriba
#todo A|B either A or B
#todo (...) a group
#todo (?:...) non-capturing version

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.com$", email):
    print("Valid")

else:
    print("Invalid")
