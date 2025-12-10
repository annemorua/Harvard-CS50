import sys

#An empty counter is started where it counts how many lines a file has, other than an empty line or a comment.
count = 0

#If the argument has only one word, the program ends.
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

#If the argument is more than two words, the program ends.
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    try:
        #Checks that the file ends in ".py".
        if sys.argv[1].endswith(".py"):
            #Opens the file that the user wrote in the argument.
            with open(sys.argv[1], "r") as file:

                #We will call all the lines of the file "l".
                l = file.readlines()

                #It goes through each line of the file, if it finds empty spaces it eliminates them.
                for line in l:
                    line = line.lstrip()

                    #If the line does not have any characters, pass.
                    if len(line) == 0:
                        continue

                    #If the line starts with a "#", pass.
                    if line.startswith("#"):
                        continue
                    else:
                        #Otherwise, add one for each line to the counter.
                        count = count + 1
        else:
            #If the file does not end with ".py", the program ends.
            sys.exit("Not a Python file")

    #If the file does not exist, the program ends.
    except FileNotFoundError:
        sys.exit("File does not exist")

#Prints the total numbers of lines.
print(count)

