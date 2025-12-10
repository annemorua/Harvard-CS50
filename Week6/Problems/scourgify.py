import sys
import csv

#If the argument has one word or two words, the program ends.
if len(sys.argv) == 1 or len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")

#If the argument is more than three words, the program ends.
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        #Checks that the file ends in ".csv".
        if sys.argv[1].endswith(".csv"):

            #Opens the file that the user wrote in the argument.
            with open(sys.argv[1], "r") as file:

                #A dictionary called "reader" is created with the file data.
                reader = csv.DictReader(file)

                #A new file is created, with the name that the user writes in the argument, where the information will be written.
                with open(sys.argv[2], "w") as file:

                    #The dictionary on which it is going to be written is created, with its respective headers.
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()

                    #Takes each line of "reader".
                    for row in reader:
                        #For each name in the "name" column, separates it into first name and last name and saves it in "writer".
                        last, first = row["name"].split(", ")

                        #For each house in the "house" column saves it in the "house" variable.
                        house = row["house"]

                        #Writes the first name, last name and house in the corresponding column.
                        writer.writerow({"first": first, "last": last, "house": house})

        # If the file does not end with ".csv", the program ends.
        else:
            sys.exit("Not a CSV file")

    #If the file does not exist, the program ends.
    except FileNotFoundError:
        sys.exit("File does not exist")

