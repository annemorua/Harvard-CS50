def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()

#Lo que está haciendo yield es hacer iterators.
