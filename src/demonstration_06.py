"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Set an O and X counter to zero
Loop over each character in the string
Do a check if it contains an "X"
    Increment the X counter
do a check if it contains an "O"
    Increment the O counter

Check if X counter is equal to O counter
    return true to the caller
otherwise
    return false to the caller

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt:str) -> bool:
#     # Set an O and X counter to zero
#     o_counter = 0
#     x_counter = 0
#     # Loop over each character in the string
#     for char in txt:
#         # Do a check if it contains an "X"
#         if char == "x":
#             # Increment the X counter
#             x_counter += 1
#             # Do a check if it contains an "X"
#         elif char == "X":
#             # Increment the X counter
#             x_counter += 1
#         # do a check if it contains an "O"
#         elif char == "o":
#             # Increment the O counter
#             o_counter += 1
#         # do a check if it contains an "O"
#         elif char == "O":
#             # Increment the O counter
#             o_counter += 1

# def XO(txt:str) -> bool:
#     # Set an O and X counter to zero
#     o_counter = 0
#     x_counter = 0
#     # Loop over each character in the string
#     for char in txt:
#         # Do a check if it contains an "X"
#         if char == "x" or char == "X":
#             # Increment the X counter
#             x_counter += 1
#         # do a check if it contains an "O"
#         elif char == "o" or char == "O":
#             # Increment the O counter
#             o_counter += 1

#     # return X counter is equal to O counter as boolean to the caller
#     return x_counter is o_counter

def XO(txt:str) -> bool:
    # Lowercase the txt
    lower_txt = txt.lower()
    # return the count of lower txt using "x" as a parameter ++ the count of lower txt using "o" as a parameter as a boolean value to the caller
    return lower_txt.count("x") == lower_txt.count("o")


print(XO("ooxx")) # ➞ True
print(XO("xooxx")) # ➞ False
print(XO("ooxXm")) # ➞ True (Case insensitive)
print(XO("zpzpzpp")) # ➞ True (Returns True if no x and o)
print(XO("zzoo")) # ➞ False