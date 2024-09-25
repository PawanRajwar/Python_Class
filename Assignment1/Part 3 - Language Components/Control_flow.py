"""
Write a Python program that asks the user for a number and determines whether it is positive, negative, or zero.
Implement a loop that continues to ask the user for a number until they enter 'exit'.
Use break to exit the loop and continue to prompt for a new number if the input is not 'exit'.

"""

while True:
    # Prompt the user to enter a number or 'exit'
    # .strip() removes any leading or trailing whitespace from the input
    user_input = input("Enter a number (or type 'exit' to quit): ").strip()

    # Check if the user wants to exit the loop
    # .lower() ensures the check is case-insensitive
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break  # Exit the loop if the user types 'exit'
    
    # Attempt to convert the input to a float
    # This allows handling both integer and decimal numbers
    try:
        number = float(user_input)
        
        # Determine if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    
    # Handle the case where the input cannot be converted to a float
    # If the input is not a valid number, a ValueError will be raised
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit' to quit.")
        # Inform the user that the input was invalid and prompt them again
