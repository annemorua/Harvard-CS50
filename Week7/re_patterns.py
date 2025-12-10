#todo . any character except a newline
#todo * 0 or more repetitions
#todo + 1 or more repetitions
#todo ? 0 or 1 repetition
#todo {m} m repetitions
#todo {m,n} m-n repetitions

import re

email = input("What's your email? ").strip()

#La "r" quiere decir que no interprete el \ de ninguna forma.
if re.search(r".+@.+\.com", email):
    print("Valid")

else:
    print("Invalid")

r".+src=(.+).+"
