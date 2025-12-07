def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))

        except ValueError:
            pass

main()

#Lo mismo pero más complicadito.
def main():
    y = get_int("What's y? ")
    print(f"y is {y}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass

main()
