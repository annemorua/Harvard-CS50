name = input("What's your name? ")

file = open("znames.txt", "w")
file.write(name)
file.close()

#Se busca poniendo en la terminal "code znames.txt".

name = input("What's your name? ")

file = open("znames.txt", "a")
file.write(f"{name}\n")
file.close()
