name = input("What's your name? ")
print("Hello Annette!")
#Va a decir decir lo que yo le "responda" a name.
print(name)
"""
Comentario gracioso.
"""
print("Bonjour, " + name)
#Es lo mismo que el de arriba.
print("Hallo,", name)

#Dice que es lo quee va al final, bien raro.
print("Hola,", end="???")
print(name)
#Dice que es lo que separa cada valor.
print("NiHao,", name, sep="???")

#Es lo mismo que .format().
print(f"Konnichiwa, {name}")

