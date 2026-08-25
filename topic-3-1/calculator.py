block = int(input("what block period is it?(if monday say 0)"))
if block == 0:
    print("class is 45 min")
    period = int(input("what period is it?"))
    if period == 1:
        print("class ends at 9:15")
    if period == 2:
        print("class ends at 10:10")
    if period == 3:
        print("class ends at 11:10")
    if period == 4:
        print("class ends at 12:05")
    if period == 5:
        print("class ends at 1:35")
    if period == 6:
        print("class ends at 2:30")
    if period == 7:
        print("class ends at 3:25")
elif block == 1:
    print("classes are 1 hr 30min")
    period = int(input("what period is it?"))
    if period == 1:
        print("class ends at 10:00")
    if period == 2:
        print("class ends at 11:40")
    if period == 3:
        print("class ends at 1:55")
    if period == 4:
        print("class ends at 3:35")
elif block == 2:
    print("classes are 1 hr 30min")
    period = int(input("what period is it?(if smart then 8)"))
    if period == 5:
        print("class ends at 10:30")
    if period == 6:
        print("class ends at 12:10")
    if period == 7:
        print("class ends at 1:55")
    if period == 8:
        print("class ends at 2:55")