# Q. Compute the greatest common divisor and least common multiple of two integers.

x = float(input("Enter a value: "))
y = float(input("Enter another value: "))

def hcf_(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           hcf = i
    return hcf

print(f"HCF : {hcf_(x, y)}, LCM : {x * y / hcf_(x, y)}")
