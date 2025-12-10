
import re
import sys

def main():
    ip = input("IPv4 Address: ")

    #If conditions are met, call the "validate" functions and print the IP.
    print(validate(ip))

#Chcks that the IP has 3 dots and 4 numbers less than or equal to 255.
def validate(ip):
    #Checks that the IP meets the conditions to be one.
    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):

        #Checks that each IP number is less than or equal to 255.
        if int(matches.group(1)) <= 255 and int(matches.group(2)) <= 255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <= 255:
            return True

        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
