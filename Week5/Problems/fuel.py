def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()

            #Calls the "convert" function and returns the percentage.
            percent = convert(fraction)

            #Calls the "gauge" function and prints the percentage or the letter according to the amount of the percentage.
            print(gauge(percent))
            break

        except(ValueError, ZeroDivisionError):
            pass

#Convert the fraction to percentage.
def convert(fraction):
    try:
        #Extracts the numerator and denominator.
        x = fraction[0]
        y = fraction[2]

        #If the donominator is 0, raises an error.
        if y == 0:
            raise ZeroDivisionError

        #If the numerator is greater than the denominator, raises an error.
        if x > y:
            raise ValueError

        #Perform the division and multiply it by 100 to have the percentage.
        percentage = round((int(x) / int(y)) * 100)
        return percentage

    #If the numerator is greater than the denominator, raises an error.
    except ValueError:
        raise ValueError

    #If the donominator is 0, raises an error.
    except ZeroDivisionError:
        raise ZeroDivisionError

#Returns the percentage or the letter according to the amount of the percentage.
def gauge(percentage):
    #If the percentage is between 1 and 99, returns the percentage with the sign.
    if 99 > percentage > 1:
        return str(percentage) + "%"

    #If the percentage is less than 1, returns "E".
    elif percentage <= 1:
        return "E"

    #If the percentage is greater than 99 but less than or equal to 100, returns "F".
    elif 100 >= percentage >= 99:
        return "F"


if __name__ == "__main__":
    main()
