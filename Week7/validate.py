email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")

else:
    print("Invalid")


      ### DE UNA FORMA MÁS PRECISA ###

username, domain= email.split("@")

if username and "." in domain:
    print("Valid")

else:
    print("Invalid")


      ### DE FORMA MÁS ESPECÍFICA ###

username, domain= email.split("@")

if username and domain.endswith(".gmail"):
    print("Valid")

else:
    print("Invalid")

