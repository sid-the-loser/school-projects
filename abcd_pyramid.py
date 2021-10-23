# Q. Generate the following patterns using nested loop. (Pattern 3)

size = 5

for i in range(size):
    code = 65
    for j in range(i+1):
        print(chr(code), end="")
        code += 1
    print()
