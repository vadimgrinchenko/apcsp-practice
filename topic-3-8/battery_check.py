charges = [62, 28, 85, 14, 47]
lowest = charges[1]
below30 = 0
atleast80 = False
for i in range (1, len(charges), 1):
    if charges[i] < lowest:
        lowest = charges[i]
    if charges[i] <= 30:
        below30 = below30 + 1
    if charges[i] >= 80:
        atleast80 = True
print(lowest)
print(below30)
print(atleast80)