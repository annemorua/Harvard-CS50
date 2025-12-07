def main():
    time = input("What time is it? ").strip(" ")

    #Checks if the time is between 7 and 8 hours.
    #Convert(time) uses what the function convert returns.
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")
    #Checks if the time is between 12 and 13 hours.
    elif convert(time) >= 12 and convert(time) <= 13:
        print("lunch time")
    #Checks if the time is between 18 and 19 hours.
    elif convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")

#This function transforms the hours into floats and transforms the minutes into what corresponds to hour, then in floats.
#Then adds them to find out the number of hours
def convert(time):
    #Separates time into hours and minutes.
    a, b = time.split(":")
    hour = float(a)
    minutes = float(b) / 60
    return hour + minutes

if __name__ == "__main__":
    main()
