#pip install mypy
#Es una librería que entiende las hints.
#$ mypy types_hints.py

def meow(n: int):
    #Los dos puntos son la type hint, dice lo que debería de ser, en este caso un int.

    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)


        ###Una especie de tests.###

def meow(n: int) -> str:
    return "meow\n" * n

    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

