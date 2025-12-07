students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#Ahora con un for.

students2 = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}
for student in students2:
    print(student, students2[student], sep=", ")

students3 = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

for student in students3:
    print(student["name"], student["house"], student["patronus"], sep=", ")
