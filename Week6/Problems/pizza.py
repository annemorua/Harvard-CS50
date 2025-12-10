from tabulate import tabulate
import sys
import csv

#If the argument has only one word, the program ends.
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

#If the argument is more than two words, the program ends.
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        #Checks that the file ends in ".csv".
        if sys.argv[1].endswith(".csv"):

            #Opens the file that the user wrote in the argument.
            with open(sys.argv[1]) as file:

                #A dictionary called "reader" is created with the file data.
                reader = csv.DictReader(file)

                #The menu is printed with the format.
                print(tabulate(reader, headers="keys", tablefmt="grid"))

        # If the file does not end with ".csv", the program ends.
        else:
            sys.exit("Not a CSV file")

    #If the file does not exist, the program ends.
    except FileNotFoundError:
        sys.exit("File does not exist")
