def main():
    twtt = input("Write a twtt: ")

    #Calls the "shorten" function and prints the twitt without vowels.
    print(shorten(twtt))

#Remove the vowels.
def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    #Checks each of the letters in the sentence, if it find a vowel, continue.
    for i in vowels:
        #Remove the vowels that are both in uppercase and in lowercase.
        word = word.replace(i.upper(), "").replace(i, "")

    return word

if __name__ == "__main__":
    main()
