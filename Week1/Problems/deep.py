answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
#Check that the input is 42, forty two or forty-two.
if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    #If not, prints "No".
    print("No")
