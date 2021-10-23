n = int(input("How much numbers do u want: "))

x, y, z = 0, 1, None

for i in range(n):
    print(x)
    z = y + x
    x = y
    y = z
