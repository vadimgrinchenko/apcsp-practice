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
            answer = math.sqrt((c^2)-(b^2))
        elif b == 0:
            answer = math.sqrt((c^2)-(a^2))
        elif c == 0:
            answer = math.sqrt((a^2)+(b^2))
        else:
            print("ERROR: ONLY NUMBER INPUT")
        print(answer)
    elif formula == "a":
        sequenceamount = 0
        continuesequence = True
        list = []
        total = 0
        answer = 0
        while continuesequence == True:
            inputforlist = input("input first number, write 'end' if done:")
            list.append(inputforlist)
            if inputforlist == "end":
                continuesequence = False
        for i in range(0, len(list) - 1, 1):
            total = total + int(list[i])
        answer = total / (len(list) - 1)
        print(answer)      
    elif formula == "l":
        print("lowest")
    else:
        print("highest")