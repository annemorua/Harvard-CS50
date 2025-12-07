expression = input("Write an arithmetic expression: ").strip(" ")

#Separates the expression into three parts, with a being the first number, b being the mathematical symbol and c being the second.
a,b,c = expression.split(" ")

if b == "+":
    print(round(float(a)+float(c),1))
elif b == "-":
    print(round(float(a)-float(c),1))
elif b == "*":
    print(round(float(a)*float(c),1))
elif b == "/":
    print(round(float(a)/float(c),1))
