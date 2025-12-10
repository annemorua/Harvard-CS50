class Student:
    #Se tiene que llamar __init__
    #todo AQUÍÍÍÍÍ.
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Missing house")
        #"self.algo" guarda lo que uno le da.
        self.name = name
        self.house = house
        self.patronus = patronus

#todo AQUÍ ESTÁÁÁÁÁ.

    def __str__(self):
        return f"{self.name} from {self.house}, {self.patronus}"



def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
