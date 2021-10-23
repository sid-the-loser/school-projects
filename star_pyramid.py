size = 5 # Determines the size of the pyramid

for i in range(size): # Loops through the size of the pyramid
    for j in range(i+1): # This for loop helps print out the stars on the basis of the value of i that slowly gets bigger as the for loop above loops through the size variable
        print("*", end="") # Prints star and ends it with nothing this means that print function won't new line all by itself
    print() # Takes the printing cursor to a new line
