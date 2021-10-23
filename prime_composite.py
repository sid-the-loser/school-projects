x = int(input("Enter the number pls: "))

prime = True

for i in range(x):
    if x != i and i > 1 and x % i == 0:
        prime = False
        break

if prime:
    print("This number is a prime number!")

else:
    print("This number is a composite number! It's divisible by", i)
