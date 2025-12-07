def main():
    time = input("What time is it? ").strip(" ")
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")
    elif convert(time) >= 12 and  convert(time) <= 13:
        print("lunch time")
    elif convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")

def convert(time):
    x, y = time.split(":")
    if y.endswith("p.m."):
        if 12 > float(x) >= 1:
            x = float(x) + 12
        elif float(x) == 12:
            x = float(x)
        minutes = y.replace("p.m.","")
        minutes = float(minutes) / 60
    elif y.endswith("a.m."):
        x = float(x)
        minutes = y.replace("a.m.", "")
        minutes = float(minutes) / 60
    else:
        x = float(x)
        minutes = float(y) / 60

    return float(x) + minutes

if __name__ == "__main__":
    main()
