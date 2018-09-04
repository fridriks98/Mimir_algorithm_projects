num_int = int(input("Input a number: "))    

max_int = num_int

while num_int >= 0:
    if max_int >= num_int:
        max_int = max_int
    else:
        max_int = num_int
    num_int = int(input("Input a number: "))	

print("The maximum is", max_int)    
