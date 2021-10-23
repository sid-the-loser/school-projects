x = input("World pls: ") # Asks to input a value and returns a string by default
x_ = "" # Variable to store reverse of values stored in "x"

for i in range(len(x), 0, -1): # Changes the value of i from n to 1
    x_ = x_ + x[i-1] # Adds the string value of the index i from x to x_

print(x, x_) # Prints the inputed string and the reversed string

if x_ == x: # Checks if x and x_ are the same, thereby determining if the sting inputed is a palindrome or not
    print("Yes, this is a palindrome!")

else: # If the if statement above if false this will run
    print(f"Nope, this is not a palindrome!")
