import emoji

sentence = input("Enter an alias: ")

#Using the emoji library, it looks for the "code" of the emoji and changes it to the emoji itself.
emoticon = emoji.emojize(sentence, language="alias")
print(emoticon)
