import random

def main():
    #Calls the funtion "get_level" and names it "nivel".
    nivel = get_level()

    #Starts an empty counter called score, which says the number of correct answers that the user had.
    score = 0

    #Create 10 mathematical operations.
    for i in range(10):
        #Calls the "generate_integer" function and generates two random numbers for each of the 10 operations.
        number1, number2 = generate_integer(nivel)

        #Solve each of the functions and saves it in "answer".
        answer = number1 + number2

        #Starts an empty counter called attempt that stores the attempts of each operation.
        attempt = 0

        #As long as the number of attempts is less than 3, continue.
        while attempt < 3:
            try:
                #Asks the user to type the answer of the operation.
                respuesta = int(input(f"{number1} + {number2} = "))

                #If the answer is the same as the on we have saved, add one point to the score and continue with the next operation.
                if respuesta == answer:
                    score = score + 1
                    break
                else:
                    # If the answer is not the same as the one we have saved print "EEE" and asks the user to type it again.
                    print("EEE")

            except ValueError:
                print("EEE")

            #For each attempt made in each operation, add one to "attempt".
            attempt = attempt + 1

        if attempt == 3:
            #When 3 attempts have already been made, it prints the operation along with the answer.
            print(f"{number1} + {number2} = {answer}")

    #At the end of all operations, it prints the total of successes.
    print("Score: " + str(score))

#A function is created that asks the user to say the level of the problems.
def get_level():
    while True:
        try:
            #A function is created that asks the user to say the level of the problems.
            level = int(input("Level: "))

            #If level is 1, 2 or 3, returns level.
            if level == 1 or level == 2 or level == 3:
                return level

            else:
                #If you enter another number, it asks the user to re-enter an accepted one.
                pass

        except ValueError:
            pass

#A function is created that creates the two random number for the operations depending on the level.
def generate_integer(level):
    #If the level is 1, create two one-digit numbers.
    if level == 1:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    #If the level is 2, create two two-digit numbers.
    elif level == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)

    #If the level is 3, create two three-digit numbers.
    elif level == 3:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)

    #Returns the two numbers created.
    return num1, num2

if __name__ == "__main__":
    main()
