name = input("What's your name? ")
#Quita espacios en blanco de la string.
name = name.strip()
#Pone en mayúscula la primera letra.
name = name.capitalize()
#Pone en mayúscula cada palabra.
name = name.title()
#Quita espacios en blanco de la string y pone en mayúsucula cada palabra.
name = name.strip().title()
#O se puede hacer todo eso desde el inicio.
name2 = input("What's your name? ").strip().title()

#Separar varias palabras de una str.
first, last = name.split(" ")

print(f"Hello, {name}")
print(f"Hallo, {name2}")
print(f"Bonjour, {first}")
print(f"NiHao, {last}")
