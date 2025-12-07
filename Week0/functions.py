def hello(to="world"):
    print("Hello,", to)
hello()
name = input("What's your name? ")
hello(name)

#Creando un main.
def main():
    name2 = input("What's your name? ")
    bye(name2)

def bye(to="world"):
    print("Bye,", to)

main()
