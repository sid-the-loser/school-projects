# Q. Input three numbers and display the leargest/smallest number.

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = float(input("Enter another number: "))

lst = [x, y, z]

lst = sorted(lst)

print(f"The greatest number is {lst[len(lst)-1]}")
print(f"Lowest number is {lst[0]}")

# or you can use min() and max() instead of sorted()
