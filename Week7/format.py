import re

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name1 = f"{first} {last}"

print(f"hello, {name1}")


# Se le escapan muchos casos.

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    name2 = f"{first} {last}"

print(f"hello, {name2}")


#De otra forma.

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name3 = f"{first} {last}"

print(f"hello, {name3}")


# De otra otra forma.

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name4 = matches.group(2) + " " + matches.group(1)

print(f"hello, {name4}")


