# Q. Write a program to input the value of x and n and print the sum of the following series:
#   Refer the question for the serieses

z = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

x = z

for i in range(n):
    x += x**i

print(x)

x = z

for i in range(n):
    if i % 2 == 0:
        x += x**i
    else:
        x -= x**i

print(x)

x = z

for i in range(n):
    if i % 2 == 0:
        x += (x/(i+1))**(i+1)
    else:
        x -= (x/(i+1))**(i+1)

print(x)

# IDK the last sum
