import random

while True:
    try:
        num = int(input("Level: "))

        #If the number is greater than zero, continue.
        if num > 0:
            break
        else:
            pass
    except ValueError:
        pass

#Takes a random number between 1 and the number the user typed.
ele = random.randint(1, num)

while True:
    try:
        #Asks the user to guess what the number would be.
        guess = int(input("Guess: "))

        #If the number is less than zero, it asks you to guess again.
        if num <= 0 or guess <= 0:
            continue

        #If the number the user guessed is less than the elected number, it prints that it is too small and asks the user to guess again.
        elif guess < ele:
            print("Too small!")

        #If the number guessed is larger than the elected one, it prints that the number is too large and asks the user to guess again.
        elif guess > ele:
            print("Too large!")

        #If the number elected and guessed are the same, print "Just right!".
        elif guess == ele:
            print("Just right!")
            break

    except ValueError:
        pass
