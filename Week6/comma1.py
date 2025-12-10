#Para guardar datos que están asociados unos a otros. csv stands for Comma-separated values.

with open("zstudents.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
#Row filas y colon columnas.

with open("zstudents.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
