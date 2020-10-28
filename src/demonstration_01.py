"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

1 + 2

label = value or an expression
a = 1
b = 2
c = a + b -> 1 + 2 -> 3 -> c = 3

return c

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
# def addition(a, b):
#     # Set a sum to the value of the expression a plus b
#     sum = a + b
#     # return our sum to the caller
#     return sum

def addition(a, b):
    # Set a sum to the value of the expression a plus b to the caller
    return a + b

print(addition(3, 2)) # -> 5
print(addition(-3, -6)) # -> -9
print(addition(7, 3)) # -> 10
