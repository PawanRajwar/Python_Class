"""
Write a python script that takes three numbers as input and prints their average using the % method for string formatting.

"""

# Take three numbers as input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Calculate the average
avg = (a + b + c) / 3

# Print the average using the % method for string formatting
print("The average of the three numbers is: %.2f" % avg)