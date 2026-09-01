import time

for x in range(360):


    clock_value_hours = 3
    clock_value_minutes = 45
    clock_value_seconds = 20

    hours = []
    minutes = []
    seconds = []

    remainingM = clock_value_minutes
    remainingH = clock_value_hours
    remainingS = clock_value_seconds

    bit_1 = remainingM % 2 
    remainingM = remainingM // 2
    bit_2 = remainingM % 2 
    remainingM = remainingM // 2
    bit_4 = remainingM % 2 
    remainingM = remainingM // 2
    bit_8 = remainingM % 2 
    remainingM = remainingM // 2
    bit_16 = remainingM % 2 
    remainingM = remainingM // 2
    bit_32 = remainingM % 2 

    minutes.append(bit_32)
    minutes.append(bit_16)
    minutes.append(bit_8)
    minutes.append(bit_4)
    minutes.append(bit_2)
    minutes.append(bit_1)

    bit_1 = remainingH % 2 
    remainingH = remainingH // 2
    bit_2 = remainingH % 2 
    remainingH = remainingH // 2
    bit_4 = remainingH % 2 
    remainingH = remainingH // 2
    bit_8 = remainingH % 2 
    remainingH = remainingH // 2
    bit_16 = remainingH % 2 
    remainingH = remainingH // 2
    bit_32 = remainingH % 2 

    hours.append(bit_32)
    hours.append(bit_16)
    hours.append(bit_8)
    hours.append(bit_4)
    hours.append(bit_2)
    hours.append(bit_1)

    bit_1 = remainingS % 2 
    remainingS = remainingS // 2
    bit_2 = remainingS % 2 
    remainingS = remainingS // 2
    bit_4 = remainingS % 2 
    remainingS = remainingS // 2
    bit_8 = remainingS % 2 
    remainingS = remainingS // 2
    bit_16 = remainingS % 2 
    remainingS = remainingS // 2
    bit_32 = remainingS % 2 

    seconds.append(bit_32)
    seconds.append(bit_16)
    seconds.append(bit_8)
    seconds.append(bit_4)
    seconds.append(bit_2)
    seconds.append(bit_1)

    print(hours)
    print(minutes)
    print(seconds)
    clock_value_seconds += 1
    if seconds == 60:
        seconds = 0
        clock_value_minutes += 1
        if minutes == 60:
            minutes = 0
            clock_value_hours += 1
    print()
    print()
    time.sleep(1)