students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)


            ###De otra forma###

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)


            ###Trabajando con las keys###

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
