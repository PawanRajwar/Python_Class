# Write a python program that takes an input number from the user, converts it to different numeric data types(integer,float, and complex) and displays the converted text.


# Prompting the user to enter a number
Value = input("Enter any number: ").strip()

# Converting the input to an integer
try:
    _int = int(Value)
    print(f"Integer value is: {_int}")
except ValueError:
    print("The input cannot be converted to an integer.")

# Converting the input to a float
try:
    _float = float(Value)
    print(f"Float value is: {_float}")
except ValueError:
    print("The input cannot be converted to a float.")

# Converting the input to a complex number
try:
    _complex = complex(Value)
    print(f"Complex value is: {_complex}")
except ValueError:
    print("The input cannot be converted to a complex number.")
    
"""
The try and except blocks in Python are used for handling exceptions—errors that occur during the execution of a program.
They allow you to write code that can gracefully handle unexpected situations without crashing the program

"""

"""
 Difference between integer , float and complex data types -
 
1. Integer (int):
 Represents whole numbers without any fractional or decimal part. 
 They can be positive, negative, or zero.
 Example: 5, -42, 0

 => Characteristics:
 No decimal point.
 Precision is unlimited (i.e., Python integers can grow as large as the memory allows).
 Common operations: addition, subtraction, multiplication, division, modulo, exponentiation.


 2. Float (float):
 Represents real numbers that include a decimal point. 
 These numbers have a fractional part and are used for more precise calculations.
 Example: 5.0, -3.14, 0.001

 => Characteristics: 
 Contains a decimal point to separate the whole part from the fractional part.
 Floating-point numbers are represented in Python using double precision (64-bit) according to the IEEE 754 standard.
 Precision is limited by the floating-point representation (up to about 15-17 significant digits).
 Common operations: similar to integers, but also include operations with decimals and real numbers.


 3. Complex (complex):
 Represents complex numbers, which have a real part and an imaginary part.
 The imaginary part is indicated by a j or J.
 Example: 3 + 4j, -2.5 + 3.1j

 => Characteristics:
 Composed of a real part (an int or float) and an imaginary part (a float) which is multiplied by j (the square root of -1).
 Used in mathematics and engineering to represent complex numbers.
 Common operations: addition, subtraction, multiplication, division, and other operations on complex numbers.    
    
"""