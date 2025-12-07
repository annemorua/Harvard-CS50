x = int(input("What's x?"))

if x % 2 == 0:
    print("Even")
#Even en español quiere decir que se puede dividir por 2.
else:
    print("Odd")

#Ahora con funciones.
def main():
    y = int(input("What's y? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Esta parte se puede acordar también así.
#def is_even(n):
#    return True if n % 2 == 0 else False

#La forma más elegante de hacerlo es así.
#def is_even(n):
#    return n % 2 == 0
main()
