"""
Write a python program that takes an integer input and prints its binary,octal and hexadecimal equivalents using for loop and bitwise operators.    
    
"""

# Function to convert a number to a specified base
def conversion(num, base):
    # Handle the special case where the number is 0
    if num == 0:
        return '0'
    
    digits = ''
    
    # Characters for bases greater than 10 (e.g., hexadecimal)
    chars = '0123456789abcdef'
    
    # Loop until num is reduced to 0
    while num > 0:
        # Find the remainder of num divided by base
        rem = num % base
        # Prepend the corresponding character for the remainder to the result string
        digits = chars[rem] + digits
        num = num // base  # Update num to be the quotient of num divided by base
    
    return digits

# Prompt the user to input a decimal number    
num = int(input("Enter any number: "))

# Print the conversions of the number to binary, octal, and hexadecimal
print(f"Decimal to Binary conversion of {num} is: {conversion(num, 2)}")
print(f"Decimal to Octal conversion of {num} is: {conversion(num, 8)}")
print(f"Decimal to Hexadecimal conversion of {num} is: {conversion(num, 16)}")
