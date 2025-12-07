# Ahora para NameError.
try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#Para cuando queremos que el usuario ponga algo específico.
while True:
    try:
        z = int(input("What's z? "))

    except ValueError:
        print("z is not an integer")
    else:
        break
print(f"z is {z}")
