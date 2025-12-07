def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #Use the two functions and multiply what they return.
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #Remove the $ from de input.
    cost = float(d.strip("$"))
    #Returns it only as a floating point number.
    return cost

def percent_to_float(p):
    #Remove the % from the input.
    percent = float(p.strip("%"))
    #Divides it by 100 to make it a percentage.
    percent = percent/100
    #Returns it only as a floating point number.
    return percent

main()
