"""
Create a Python script that takes two numbers as input and prints whether both numbers are even, odd, or one of each using relational and logical operators.

"""

# Take two numbers as input from the user
# Convert the input strings to integers using int()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if both numbers are even
# A number is even if it has no remainder when divided by 2
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")

# Check if both numbers are odd
# A number is odd if it has a remainder of 1 when divided by 2
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")

# If neither of the above conditions are true,
# it means one number is even and the other is odd
else:
    print("One number is even and the other is odd.")
