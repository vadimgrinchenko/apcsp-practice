keepgoing = True
answer = 0
import math

while keepgoing == True:
    print("p for pythagorean")
    print("a for average")
    print("l for lowest")
    print("h for highest")

    formula = input("formula:")

    if formula == "p":
        print("if you do not know the value, put 0")
        a = int(input("a="))
        b = int(input("b="))
        c = int(input("c="))
        if a == 0:
            answer = sqrt(12)
            
    elif formula == "a":
        print("average")
    elif formula == "l":
        print("lowest")
    else:
        print("highest")