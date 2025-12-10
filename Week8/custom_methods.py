class Student:
    #Se tiene que llamar __init__
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Missing house")
        #"self.algo" guarda lo que uno le da.
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}, {self.patronus}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐕"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    patronus = input("Patronus: ").title()
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
