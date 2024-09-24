#Write a Python program that takes a user's first and last name as input and prints them in reverse order with a space between them.

# Prompting the user to enter their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Printing the names in reverse order
print(f"{last_name} {first_name}") # Using f-string which allow for the easy and efficient embedding of expressions within string literals.

# Reversing the order of both the first and last names, as well as their overall positions.

# Prompting the user to enter their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Reversing the order of characters in each name
reversed_first_name = first_name[::-1] # The [::-1] slice notation reverses the string
reversed_last_name = last_name[::-1]

# Print the names in reverse order with reversed characters
print(f"{reversed_last_name} {reversed_first_name}")

