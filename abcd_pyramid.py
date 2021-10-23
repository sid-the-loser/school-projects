size = 5

for i in range(size, 0, -1):
    code = 65
    for j in range(i):
        print(chr(code), end="")
        code += 1
    print()
