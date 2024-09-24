# script.py

import sys

# Defining name and course name.
Name = "Pawan Singh Rajwar"
course_name = "Python Programming"

# Get Python version
# The import sys statement makes the sys module available in your script. 
# This module provides functionality related to the Python runtime environment and can be used for various purposes.
python_version = sys.version


# Print the information
# The f in f"Name: {name}" is part of an f-string, which stands for "formatted string literal".
# An f-string is a string literal prefixed with f or F before the opening quotation mark. 
# The primary purpose of f-strings is to allow for the easy and efficient embedding of expressions within string literals.
print(f"Name: {Name}")
print(f"Course Name: {course_name}")
print(f"Python Version: {python_version}")
