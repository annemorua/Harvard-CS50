greeting = input("Say a greeting: ").lower().strip(" ")
#Just the word "hello".
if greeting.startswith("hello"):
    print("$0")
#Any word that starst with h.
elif greeting.startswith("h"):
    print("$20")
#Any other word that is not "hello" or begins with h.
else:
    print("$100")

