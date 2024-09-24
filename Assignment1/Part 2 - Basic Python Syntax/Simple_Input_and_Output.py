"""
Create a python script that calculates the area of rectangle. 
The script should:

 * Prompt the user to enter the length and width of a rectangle.
 * calculate the area of rectangle  
 * Display the result using print() function
 * Modify the rectangle area program to format the output so that it displays the area with two decimal places
    
"""
# Prompting the user to enter the length and width of the rectangle
# .strip() is used to remove any leading or trailing whitespace from the input
length = float(input("Enter the length of the rectangle: ").strip())
width = float(input("Enter the width of the rectangle: ").strip())

# Calculating area of rectangle
area = length * width 
# format area upto two decimal places
format_area = "{:.2f}".format(area)
print(f"area of rectangle with length {length} and width {width} is: {format_area}")
