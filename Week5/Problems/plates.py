def main():
    plate = input("Plate: ").strip(" ")

    #If all the conditions of the "is_valid" function are satisfied, prints "Valid".
    if is_valid(plate):
        print("Valid")

    #If the conditions are not satisfied, prints "Invalid".
    else:
        print("Invalid")

#Determines which plates are valid.
def is_valid(plate):
    #Checks that the length of the plate is greater then two but less than or equal to 6.
    if len(plate) < 2 or len(plate) > 6:
        return False

    #Checks that if the first and second characters are not letters, returns false.
    elif not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    #Checks that if the plate is not made entirely of letters or numbers, returns false.
    elif not plate.isalnum():
        return False

    #Passes through each character of the plate.
    for i in range(len(plate)):

        #If finds the first numebr, and it is a 0, returns false.
        if plate[i].isdigit():
            if plate[i] == "0":
                return False

            #If it is not 0, checks that all the characters after the first number are also numbers.
            numpart = plate[i:]
            if numpart.isdigit():
                return True

            else:
                return False
    return True

if __name__ == "__main__":
    main()
