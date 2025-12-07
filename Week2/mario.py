print("Este imprime una columna de 3 bloques.")
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

print("Este imprime una fila de 4 bloques de signo de pregunta.")
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

print("Este imprime un cuadrado que aparece más tarde en el juego.")
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #Print brick
            print("#", end="")
        print()

main()

#Más simplificado.
print("")
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()

#De otra forma.
print("")
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
