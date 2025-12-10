import sys
import random
from pyfiglet import Figlet

#We check that the argument has only one word.
if len(sys.argv) == 1:
    sentence = input("Just write smth: ")

    #Using the random library, we chose a random font.
    randomfont = random.choice(Figlet().getFonts())

    #Takes the extracted font and puts it to the sentence written by the user.
    exfont = Figlet(font=randomfont)
    print(exfont.renderText(sentence))

#If the third argument, which is the font, is not in the font list, end the program.
elif sys.argv[2] not in Figlet().getFonts():
    sys.exit("Invalid usage")

#If the second argument contains the word "-f" or "--font", continue.
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    sentence = input("Just write smth: ")

    #Extracts the font of the third argument and puts it to the sentence the user wrote.
    exfont = Figlet(font=sys.argv[2])
    print(exfont.renderText(sentence))

#If none of the conditions are satisfied, the program ends.
else:
    sys.exit("Invalid usage")
