camel = input("Write a sentence: ")

for i in camel:
    #If it finds an uppercase letter, it replace that letter with an "_" and the same letter but in lowercase.
    if i.isupper():
        camel = camel.replace(i, "_" + i.lower())
print(camel)


