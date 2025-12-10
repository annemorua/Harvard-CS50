name = input("What's your name? ")

with open("znames.txt", "a") as file:
    file.write(f"{name}\n")
