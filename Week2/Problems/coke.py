due = 50
#As long as due is greater than 0, it will continue to prompting "Insert a coin".
while due > 0:
    coin = input("Insert Coin: ")
    #If the coin is 25, 10 or 5, continue.

    if coin == "25" or coin == "10" or coin == "5":
        #From the original 50 it substracts the value of the inserted coin and saves the new value of due.
        due = due - int(coin)

        if due > 0:
            #If due is still greater than 0, prints "Amount due" and the new value of due.
            print("Amount Due: " + str(due))

        else:
            #If due is equal to or less than 0, prints "Change owed" and the leftover value, which is the new value that took due.
            print("Change Owed: " + str(abs(due)))

    else:
        #If the coin is another, it asks again to "Insert a coin".
        print("Amount Due: 50")

#When the counter reaches 0 or less, it stops.
