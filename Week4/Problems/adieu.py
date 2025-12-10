import inflect

#Starts an instanc with which you can do various formatting operations.
stru = inflect.engine()

#An empty list is started where the names entered by the user will be saved.
names = []
while True:
    try:
        name =  input("Name: ")

        #Append the names to the "names" list.
        names.append(name)

        #Takes the names from the list, separates each of the names with a comma except the las two, which separates the with an "and".
        #If there are only two names, separate the with "and".
        comma = stru.join(names)

    except EOFError:
        break

#Prints the phrase with the formatted names.
print("Adieu, adieu, to " + comma)

