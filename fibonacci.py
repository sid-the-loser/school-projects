# Q. Display the terms of a Fabonacci series.

n = int(input("How much numbers do u want: "))

x, y = 0, 1

for i in range(n):
    print(x)
    z = y + x
    x = y
    y = z
