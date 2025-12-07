print("¡¡¡Números enteros!!!")
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)
#O se puede hacer también de esta forma.
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

print("¡¡¡Números con decimales!!!")
#Ahora con floats.
a = float(input("What's a? "))
b = float(input("What's b? "))
c = round(a + b)
print(a + b)
#Va a redonder la suma.
print(c)

print(f"{c:,}")

print("¡¡¡Ahora divisiones!!!")
#Divisones
e = float(input("What's e? "))
f = float(input("What's f? "))
g = e / f
print(g)
#Ahora redondeando.
g = round(e / f, 2)
print(g)
#Lo mismo del anterior.
print(f"{g:.2f}")
