x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = float(input("Enter another number: "))

if x == y == z:
    print(f"{x} = {y} = {z}")

elif x > y:
    if x > z:
        print(f"{x} is the greatest number")
    else:
        print(f"{z} is the greatest number")

else:
    if y > z:
        print(f"{y} is the greatest number")
    else:
        print(f"{z} is the greatest number")
