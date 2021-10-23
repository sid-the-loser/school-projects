# Q. Determine wheather a number is a perfect number, and armstrong number or a palindrome.

x = int(input("Enter the number here: "))

x = [x, str(x)]

x_ = ""

for i in range(len(x[1]), 0, -1):
    x_ = x_ + x[1][i-1]

if x_ == x[1]:
    print("This number is a palindrome!")

else:
    print("This number is not a palindrome!")

x__ = 0

for i in x_:
   x__ += int(i)**3

if x__ == x[0]:
    print("This number is an armstrong number!")
else:
    print("This number is not an armstrong number!")

x_ = 0

for i in range(x[0]):
    if x[0] % (i+1) == 0:
        x_ += i+1

if x_//2 == x[0]:
    print("This number is perfect!")

else:
    print("This number is not perfect!")
