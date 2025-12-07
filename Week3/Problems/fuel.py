while True:
    try:
        #Asks to enter the amount of fuel as a fraction.
        fraction = input("Fraction: ").split("/")

        x = int(fraction[0])
        y = int(fraction[1])
        #Converts it into percentage.
        percent = round((x / y) * 100)

        #If the percentage is grater than 100, it asks you to enter another fraction again.
        if percent > 100:
            continue

        #If the percentage is between 1 and 99, prints the percentage.
        elif 99 > percent > 1:
            print(str(percent) + "%")

        #If the percentage is less than 1, prints an "E".
        elif percent <= 1:
            print("E")

        #If the percentage is greater than 99 but less than or equal to 100, prints an "F".
        elif 100 >= percent >= 99:
            print("F")

    #If the user types something other than a number, it asks them to type a fraction again.
    except ValueError:
        pass

    #If the user divides by 0, it asks them to type a fraction again.
    except ZeroDivisionError:
        pass

    else:
        break
