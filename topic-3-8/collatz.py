numberamounts = []
for x in range (1,1000):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            steps = steps + 1
            print(x)
        else:
            x = x * 3 + 1
            steps = steps + 1
            print(x)
    print("it is equal to 1")
    print(steps)
    numberamounts.append(steps)
print(numberamounts)