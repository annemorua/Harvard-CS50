twtt = input("Write a twtt: ")

vowels = ["a","e","i","o","u"]

for i in vowels:
    #If there is a vowel in uppercase in twtt, replace that vowel with nothing.
    twtt = twtt.replace(i.upper(), "")
    #If there is a vowel in twtt, replace that vowel with nothing.
    twtt = twtt.replace(i, "")
print(twtt)
