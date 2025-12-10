import re
import sys

def main():
    html = input("HTML: ")

    #Calls the "parse" function and prints it.
    print(parse(html))

#Convert the link into the expected format.
def parse(s):
    #Looks for "youtube" in the HTML that the user wrote.
    if "youtube" in s:

        #Looks for "src=" to be before two quotation marks.
        if matches := re.search(r".+src=\"(.+)\".+", s):

            #Takes what's in the middle of those first quotation marks.
            long_weird = matches.group(1)

            #"long_weird" took all the characters after the first quote, but the other quote stayed there, so it is searched.
            place = matches.group(1).find("\" ")

            #If the quote does not exist, continue.
            if place == -1:

                #Check that it has the proper format.
                if pure := re.search(r"((?:https?)://(?:www\.)?(.+))", long_weird):

                    #Specifically look for a slash in a range of characters.
                    place = pure.group(1).find("/", 24, 35)

                    #Searches all characters from the first to "place".
                    char = pure.group(1)[0:place]

                    #Replace all characters with a new string and leave the rest of the link the same.
                    link1 = pure.group(1).replace(char, "https://youtu.be")

                    return link1

            else:
                #Check that it has the proper format.
                if pure := re.search(r"((?:https?)://(?:www\.)?(.+))", long_weird):

                    #Since the other quote exists, the position of this quote is searched.
                    cut = pure.group(1).find("\" ")

                    #Searches for all characters from the first to the one before the quote.
                    part1 = long_weird[0:cut]

                    #Specifically look for a slash in a range of characters.
                    place = pure.group(1).find("/", 24, 35)

                    #Searches for all characters from the first to the forward slash.
                    char = pure.group(1)[0:place]

                    #Replace all characters with a new string and leave the rest of the link the same.
                    link2 = part1.replace(char, "https://youtu.be")
                return link2

if __name__ == "__main__":
    main()
