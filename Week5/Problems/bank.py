def main():
    greeting = input("Say a greeting: ").strip(" ")

    #Calls the "value" function and prints the amount of money.
    print(value(greeting))

def value(greeting):
    #Makes the greeting lowercase.
    greeting = greeting.lower()

    #If the greeting starts with "hello", returns 0 dollars.
    if greeting.startswith("hello"):
        return "$0"

    #If the greeting starts with "h", returns  20 dollars.
    elif greeting.startswith("h"):
        return "$20"

    #Otherwise, returns 100 dollars.
    else:
        return "$100"

if __name__ == "__main__":
    main()

