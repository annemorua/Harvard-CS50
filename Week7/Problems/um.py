import re

def main():
    sentence = input("Sentence: ")

    #Calls the "count" function and prints the number of "ums".
    print(count(sentence))

#Returns the amount of "ums" in the sentence.
def count(s):
    #Save only the "ums" in a list.
    ums = re.findall(r"\bum\b", s.lower())

    #Count how many "ums" are on the list.
    counter = len(ums)

    return counter

if __name__ == "__main__":
    main()
