"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

To get the perimeter of a rectangle we could use either (L * 2 + W * 2) or (L + W) * 2

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
# def find_perimeter(length, width):
#     # Set a perimeter to the value of the expression (Length + Width) * 2
#     perimeter = (length + width) * 2
#     # Return the perimeter to the caller
#     return perimeter

def find_perimeter(length, width):
    # Return the value of the expression (Length + Width) * 2
    return (length + width) * 2


print(find_perimeter(6, 7)) # ➞ 26
print(find_perimeter(20, 10)) # ➞ 60
print(find_perimeter(2, 9)) # ➞ 22
