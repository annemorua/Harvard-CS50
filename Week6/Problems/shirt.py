import sys
from PIL import Image, ImageOps

#Take the second and third words, in lowercase, so that I don't have to write much.
arg1 = sys.argv[1].lower()
arg2 = sys.argv[2].lower()

#If the argument has one word or two words, the program ends.
if len(sys.argv) == 1 or len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")

#If the argument is more than three words, the program ends.
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        #Checks that both files end in ".jpeg", ".jpg" or ".png".
        if arg1.endswith((".jpeg", ".jpg", ".png")) and arg2.endswith((".jpeg", ".jpg", ".png")):
            pass

            #Checks that both files have the same ending.
            if arg1[-4:-1] == arg2[-4:-1]:

                #Muppet image.
                photo = Image.open(arg1)
                #Image of the shirt, which is located in the directory.
                shirt = Image.open("shirt.png")

                #Adjust the photo to the specific size.
                photo = ImageOps.fit(photo, (600,600))

                #Paste the image of the shirt over the image of the photo.
                photo.paste(shirt, shirt)

                #The new image is saved to the file that the user writes in the argument.
                photo.save(arg2)

            else:
                #If both files end differently, the program ends.
                sys.exit("Input and output have different extensions")

        else:
            sys.exit("Invalid output")

    #If the file does not exist, the program ends.
    except FileNotFoundError:
        sys.exit("File does not exist")
