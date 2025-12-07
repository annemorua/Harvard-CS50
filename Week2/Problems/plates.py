def main():
    plate = input("Plate: ").strip(" ")
    #If the function is True, prints "Valid".
    if is_valid(plate):
        print("Valid")
    #If its False, prints "Invalid".
    else:
        print("Invalid")

def is_valid(plate):
    #If the plate lenght is less than two characters or greater than six, returns False.
    if len(plate) < 2 or len(plate) > 6:
        return False

    #Checks that the first and second characters are letters, if they are not, returns False.
    elif not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    #Checks if there are periods or punctuation marks, if there is not, returns False.
    elif not plate.isalnum():
        return False

    #Checks the length of the plate, then count from 0 to whatever the plate measures.
    for i in range(len(plate)):
        #Checks the characters until it finds the first number, if it is a 0, returns False.
        if plate[i].isdigit():
            if plate[i] == "0":
                return False

            #If the first number is not a 0, the variable numpart takes the values that follows that number.
            numpart = plate[i:]
            #If all values are numbers, returns True.
            if numpart.isdigit():
                return True

            else:
                return False
    return True

main()
