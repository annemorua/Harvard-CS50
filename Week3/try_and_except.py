x = int(input("What's x? "))
#No da error cuando solo se ponen números enteros.
print(f"x is {x}")

#Con este si puedo meter algo que no sea números sin que de ValueError.
try:
    y = int(input("What's y? "))
    print(f"y is {y}")
except ValueError:
    print("y is not an integer")


