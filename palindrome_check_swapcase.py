x = input("Enter the string: ")
x_ = ""

for i in range(len(x), 0, -1):
    x_ = x_ + x[i-1]
    
if x_ == x:
    print("Yes, this is a palindrome!")
else:
    print(f"Nope, this is not a palindrome!")

print(x.swapcase())
