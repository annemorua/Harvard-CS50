for i in [0,1,2]:
    print("hola")

#Para diferenciar los fors.
print("")
print("¡¡¡Cambio!!!")
print("")

for i in range(3):
    print("hello")

#Para diferenciar los fors.
print("")
print("¡¡¡Cambio!!!")
print("")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("bonjour")

#Con una función.
def main():
    number = get_number()
    saludo(number)

def get_number():
    while True:
        x = int(input("What's x? "))
        if x > 0:
            break
    return x
def saludo(x):
    for _ in range(x):
        print("hallo")

main()
