# Q. Generate the following patterns

"""
  i    ii    iii
-----------------
*     12345 A
**    1234  AB
***   123   ABC
****  12    ABCD
***** 1     ABCDE

"""

size = 5

print("\nPattern i\n")

for i in range(size):
    for j in range(i+1):
        print("*", end="")
    print()

print("\nPattern ii\n")

for i in range(size, 0, -1):
    for j in range(i):
        print(j+1, end="")
    print()

print("\nPattern iii\n")

for i in range(size):
    code = 65
    for j in range(i+1):
        print(chr(code), end="")
        code += 1
    print()
