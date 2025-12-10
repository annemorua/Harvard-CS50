import sys
#Para esto hay que usar la terminal
#print("Hello, my name is", sys.argv[1])
#si se pone cero en sys.argv[0] lo que tira es "hello, my name is sys.py".

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments.")

#U otra forma.
if len(sys.argv) < 2:
    print("Too few arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments.")
else:
    print("Hello, my name is", sys.argv[1])

#De una forma más bonita según Malan.
#Check for errors.
if len(sys.argv) < 2:
    print("Too few arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments.")

#Print name tags.
print("Hello, my name is", sys.argv[1])
