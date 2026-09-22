productinfo = input("Product Code: ")
destination = 0

shape = productinfo[0:4]   
color = productinfo[4:7]    
size = int(productinfo[7:10])   
mass = int(productinfo[10:14])
condition = productinfo[14:15]

if condition == "D" or mass > 2000 or size > 50:
    destination = "Inspect"
else:
    if shape == "BALL":
        if size > 10 and color == "RED":
            destination = "B" 
        else:
            destination = "A"   
    else:
        if shape == "CUBE":
            if color == "GRN" or color == "BLU" and size < 10:
                destination = "C"
            else:
                destination = "D"
        else:
            destination = "E"
print(destination)

