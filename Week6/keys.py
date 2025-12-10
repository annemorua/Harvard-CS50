students = []

with open("zstudents.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

#Ordena los nombres.
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

#for student in sorted(students, key=get_name):
 #   print(f"{student['name']} is in {student['house']}")


#Ordena los casas.
def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")
