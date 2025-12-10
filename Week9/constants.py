MEOWS = 3

for _ in range(MEOWS):
    print("meow")


        ###Ahora con class###

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(MEOWS):
            print("meow")

cat = Cat()
cat.meow()
