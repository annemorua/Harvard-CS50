#A library is imported that checks by itself whether an email address is valid or invalid.
import validators

email = input("What's your email address? ")

#Returns a boolean assigned the name "val".
val = validators.email(email)

#If it returns True, it prints "Valid".
if val == True:
    print("Valid")

#If it returns False, it prints "Invalid".
else:
    print("Invalid")
