def main():
    emoji = input("Write a sentence: ")
    #Calls the convert function.
    sentence = convert(emoji)
    print(sentence)

def convert(emoticon):
    #Replace all ":)" with smiley emoticons.
    converted1 = emoticon.replace(":)", "🙂")
    #One it changed all ":)", use converted1 and replace all ":(" with frown emoticons.
    converted2 = converted1.replace(":(", "🙁")
    return converted2

main()

