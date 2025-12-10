import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    #Today takes the value of the current day.
    today = date.today()

    birth = input("Date of birth: ")

    #If birth does not have the correct format, the program ends.
    try:
        birth = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")

    #Calls the "minutes" function.
    totalmins = minutes(birth, today)

    #Calls the "words" function and capitalize the first letter of the sentence.
    inwords = words(totalmins).capitalize()
    print(inwords + " minutes")

#Calculate the number of minutes between the current date and the date the user type.
def minutes(today, birth):
    #Get the number of years between the current date and the date the user writes.
    years = abs(today - birth)
    #Calculate the number of days in those years and multiply them by 24 and 60 to get the minutes.
    mins = years.days * 24 * 60
    return mins

#Writes the number of minutes in words.
def words(n):
    #The function that writes the number of minutes in words.
    words = p.number_to_words(n)
    #Removes the "and" from the sentence.
    words = words.replace(" and", "")
    return words

if __name__ == "__main__":
    main()
