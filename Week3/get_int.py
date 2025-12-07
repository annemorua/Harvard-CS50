def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))

        except ValueError:
            print("x is not an integer")
        else:
            #O para compactar poner aquí el return x en lugar del break.
            break
    return x

main()

#O incluso aún más compacto.
def main():
    y = get_int()
    print(f"y is {y}")


def get_int():
    while True:
        try:
            return int(input("What's z? "))

        except ValueError:
            print("z is not an integer")

main()
