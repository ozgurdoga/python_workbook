from math import log10

#Create a program that reads two integers, a and b, from the user. Your program shouldcompute and #display:
a = int(input())
b = int(input())
print(f"Sum of a + b = {a+b}")
print(f"The product of a and b = {a*b}")
print(f"The quotient when a is divided by b {a/b}")
print(f"The remainder when a is divided by b = {a%b}")
print(log10(a))
print(a**b)