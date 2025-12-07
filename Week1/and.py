score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Cambiando el orden de las cosas.
score2 = int(input("Score: "))
if 90 <= score2 and score <= 100:
    print("Grade: A")
elif 80 <= score2 and score < 90:
    print("Grade: B")
elif 70 <= score2 and score < 80:
    print("Grade: C")
elif 60 <= score2 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Ahora sin hacer dos preguntas.
score3 = int(input("Score: "))
if score3 >= 90:
    print("Grade: A")
elif score3 >= 80:
    print("Grade: B")
elif score3 >= 70:
    print("Grade: C")
elif score3 >= 60:
    print("Grade: D")
else:
    print("Grade: F")
