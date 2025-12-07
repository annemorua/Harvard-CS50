sentence = input("Write a fruit: ").strip(" ").lower()

fruits = {"apple" : 130,
          "avocado": 50,
          "cantaloupe" : 50,
          "honeydew melon" : 50,
          "pineapple" : 50,
          "strawberries" : 50,
          "tangerine" : 50,
          "banana" : 110,
          "grapefruit" : 60,
          "nectarine" : 60,
          "peach" : 60,
          "grapes" : 90,
          "kiwifruit": 90,
          "lemon" : 15,
          "lime" : 20,
          "orange" : 80,
          "watermelon" : 80,
          "pear" : 100,
          "sweet cherries" : 100,
          "plums" : 70}

#If the fruit is in the dictionary, prints the calories.
if sentence in fruits:
    print("Calories: ", fruits[sentence])
