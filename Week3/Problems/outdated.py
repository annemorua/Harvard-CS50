months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    try:
        #The first letter has to be capitalized to match the month dictionary.
        mdy = input("Write a date: ").title().strip(" ")

        #If the input has a "/", continue.
        if "/" in mdy:

            #They are separated into month, day and year.
            numbers = mdy.split("/")
            d = numbers[1]
            m = numbers[0]
            y = numbers[2]

            #If all parts of numbers are numbers, continue.
            if all(i.isdigit() for i in numbers):

                #If m is between 1 and 12 and d between 1 and 31, continue.
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:

                    #Create a list with the date as it should be.
                    lstnumbers = [y, m, d]

                    #For eache number in lstnumbers, checks if it has less than two characters.
                    for i in lstnumbers:
                        if len(i) < 2:

                            #If yes, adds a 0 in front.
                            ceros = f"{int(i):02}"
                            #Replaces it in lstnumbers in the same position in which it found it.
                            lstnumbers[lstnumbers.index(i)] = ceros

                    #Takes lstnumbers and joins each element into a string with a "-".
                    date = "-".join(lstnumbers)
                    print(date)
                    break

                else:
                    #If the conditions are not satisfied, ask again to enter a date.
                    pass
            else:
                #If the conditions are not satisfied, ask again to enter a date.
                pass

        else:
            #They are separated into month, day with a comma and year.
            letters = mdy.split(" ")
            d = letters[1]
            m = letters[0]
            y = letters[2]

            #If the first character is a month of the year, looks for the position in which it is found in he dictionary and adds a 1 to it.
            if m in months:
                m = months.index(m) + 1

                #If the character that corresponds to day has a comma, it is removed.
                if "," in d:
                    d = d.replace(",", "")

                    #A list is created with the correct date order.
                    lstletters = [y, str(m), d]

                    #Checks that the month and year are numbers and that the day is between 1 and 31.
                    if str(m).isdigit() and y.isdigit() and 1 <= int(d) <= 31:

                        #For each item in lstletters it checks if it has more than two characters.
                        for i in lstletters:
                            if len(str(i)) < 2:

                                #If yes, adds a 0 in front.
                                ceros = f"{int(i):02}"
                                #Replaces it in lstletters in the same position in which it found it.
                                lstletters[lstletters.index(i)] = ceros

                        #Takes lstletters and joins each element into a string with a "-".
                        date = "-".join(lstletters)
                        print(date)

                        break
                #If it does not have a comma in the character that corresponds to say, it asks you write a date again.
                else:
                    pass
            else:
                #If the conditions are not satisfied, ask again to enter a date.
                pass

    except EOFError:
        break

