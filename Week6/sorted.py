names = []

with open("znames.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#MÁS SENCILLO.
with open("znames.txt") as file:
    for line in sorted(file):
        print("hello," ,line.rstrip())

#Para ordenar de de Z a A: sorted(iterable, /, *, key=None, reverse=True).
