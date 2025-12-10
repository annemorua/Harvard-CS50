with open("../znames.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    #print("hello,", line, end="")     Son lo mismo en este caso.
    print("hello,",line.rstrip())

#De otra forma.

with open("../znames.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())



