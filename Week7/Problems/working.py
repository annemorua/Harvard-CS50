import re

def main():
    hours = input("Hours: ")

    #Calls the "convert" function and prints it.
    print(convert(hours))

#Put the hours in 24 hour format.
def convert(s):
    #Checks that the hours are in the correct format.
    if twel := re.search(r"^(\d{1,2})(:[0-5][0-9])? (A|P)M to (\d{1,2})(:[0-5][0-9])? (A|P)M$", s):

        #Saves the first hour as an integer.
        h1 = int(twel.group(1))
        #Saves the first minutes, if there are no minutes, add ":00" next to the hour.
        m1 = twel.group(2)
        if m1 == None:
            m1 = ":00"
        #Saves if the first time is AM or PM.
        half1 = twel.group(3)

        #Saves the second hour as an integer.
        h2 = int(twel.group(4))
        #Saves the second minutes, if there are no minutes, add ":00" next to the hour.
        m2 = twel.group(5)
        if m2 == None:
            m2 = ":00"
        #Saves if the second time is AM or PM.
        half2 = twel.group(6)

        #Checks if the time of both hours is AM, if yes and also it is 12, change the hour to 0.
        if half1 == "A" or half2 == "A":
            if h1 == 12 or h2 == 12:
                h1 = 0
                h2 = 0

        #Checks if the time of the first hour is PM, if yes and also it is 12, add to the hour 12.
        if half1 == "P":
            if h1 != 12:
                h1 = h1 + 12

        #Checks if the time of the second hour is PM, if yes and also it is 12, add to the hour 12.
        if half2 == "P":
            if h2 != 12:
                h2 = h2 + 12

        #Returns the hours with the new format.
        return f"{str(h1).zfill(2)}{m1} to {str(h2).zfill(2)}{m2}"

    raise ValueError

if __name__ == "__main__":
    main()
